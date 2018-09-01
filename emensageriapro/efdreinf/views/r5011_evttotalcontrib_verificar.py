#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.r5011.models import *
from emensageriapro.r5011.forms import *
import os


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def txt_xml(texto):
    texto = str(texto)
    texto = texto.replace(">",'&gt;')
    texto = texto.replace("<",'&lt;')
    texto = texto.replace("&",'&amp;')
    texto = texto.replace('"','&quot;')
    texto = texto.replace("'",'&apos;')
    return texto



def verificar(request, hash, slug=0):
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.session['usuario_id']   
        dict_hash = get_hash_url( hash )
        r5011_evttotalcontrib_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5011_evttotalcontrib')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using( db_slug ), excluido = False, id = r5011_evttotalcontrib_id)
        r5011_evttotalcontrib_lista = r5011evtTotalContrib.objects.using( db_slug ).filter(id=r5011_evttotalcontrib_id, excluido = False).all()
        
    
        r5011_regocorrs_lista = r5011regOcorrs.objects.using(db_slug).filter(r5011_evttotalcontrib_id__in = listar_ids(r5011_evttotalcontrib_lista) ).filter(excluido=False).all()    
        r5011_infototalcontrib_lista = r5011infoTotalContrib.objects.using(db_slug).filter(r5011_evttotalcontrib_id__in = listar_ids(r5011_evttotalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rtom_lista = r5011RTom.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_infocrtom_lista = r5011infoCRTom.objects.using(db_slug).filter(r5011_rtom_id__in = listar_ids(r5011_rtom_lista) ).filter(excluido=False).all()    
        r5011_rprest_lista = r5011RPrest.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rrecrepad_lista = r5011RRecRepAD.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rcoml_lista = r5011RComl.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rcprb_lista = r5011RCPRB.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r5011_evttotalcontrib'
        context = {
            'r5011_evttotalcontrib_lista': r5011_evttotalcontrib_lista,
            'r5011_evttotalcontrib_id': r5011_evttotalcontrib_id, 
            'r5011_evttotalcontrib': r5011_evttotalcontrib, 
            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
    
            'r5011_regocorrs_lista': r5011_regocorrs_lista,    
            'r5011_infototalcontrib_lista': r5011_infototalcontrib_lista,    
            'r5011_rtom_lista': r5011_rtom_lista,    
            'r5011_infocrtom_lista': r5011_infocrtom_lista,    
            'r5011_rprest_lista': r5011_rprest_lista,    
            'r5011_rrecrepad_lista': r5011_rrecrepad_lista,    
            'r5011_rcoml_lista': r5011_rcoml_lista,    
            'r5011_rcprb_lista': r5011_rcprb_lista,
        }
        if for_print == 2:
            #return render_to_pdf('%s/r5011_evttotalcontrib_verificar.html' % r5011_evttotalcontrib.versao, context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(request=request,
                                           template='%s/r5011_evttotalcontrib_verificar.html' % r5011_evttotalcontrib.versao,
                                           filename="r5011_evttotalcontrib.pdf",
                                           context=context,
                                           show_content_in_browser=True,
                                           cmd_options={'margin-top': 5,
                                                        'margin-bottom': 5,
                                                        'margin-right': 5,
                                                        'margin-left': 5,
                                                        "zoom": 3,
                                                        "viewport-size": "1366 x 513",
                                                        'javascript-delay': 1000,
                                                        'footer-center': '[page]/[topage]',
                                                        "no-stop-slow-scripts": True},
                                           )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/r5011_evttotalcontrib_verificar.html' % r5011_evttotalcontrib.versao, context)
            filename = "%s.xls" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/r5011_evttotalcontrib_verificar.html' % r5011_evttotalcontrib.versao, context)
            filename = "%s.csv" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, '%s/r5011_evttotalcontrib_verificar.html' % r5011_evttotalcontrib.versao, context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_r5011(r5011_evttotalcontrib_id, db_slug):
    from django.template.loader import get_template
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using( db_slug ), excluido = False, id = r5011_evttotalcontrib_id)
        r5011_evttotalcontrib_lista = r5011evtTotalContrib.objects.using( db_slug ).filter(id=r5011_evttotalcontrib_id, excluido = False).all()
    
        r5011_regocorrs_lista = r5011regOcorrs.objects.using(db_slug).filter(r5011_evttotalcontrib_id__in = listar_ids(r5011_evttotalcontrib_lista) ).filter(excluido=False).all()    
        r5011_infototalcontrib_lista = r5011infoTotalContrib.objects.using(db_slug).filter(r5011_evttotalcontrib_id__in = listar_ids(r5011_evttotalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rtom_lista = r5011RTom.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_infocrtom_lista = r5011infoCRTom.objects.using(db_slug).filter(r5011_rtom_id__in = listar_ids(r5011_rtom_lista) ).filter(excluido=False).all()    
        r5011_rprest_lista = r5011RPrest.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rrecrepad_lista = r5011RRecRepAD.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rcoml_lista = r5011RComl.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()    
        r5011_rcprb_lista = r5011RCPRB.objects.using(db_slug).filter(r5011_infototalcontrib_id__in = listar_ids(r5011_infototalcontrib_lista) ).filter(excluido=False).all()
        context = {
            'base': r5011_evttotalcontrib,
            'r5011_evttotalcontrib_lista': r5011_evttotalcontrib_lista,
            'r5011_evttotalcontrib_id': int(r5011_evttotalcontrib_id), 
            'r5011_evttotalcontrib': r5011_evttotalcontrib,
    
            'r5011_regocorrs_lista': r5011_regocorrs_lista,    
            'r5011_infototalcontrib_lista': r5011_infototalcontrib_lista,    
            'r5011_rtom_lista': r5011_rtom_lista,    
            'r5011_infocrtom_lista': r5011_infocrtom_lista,    
            'r5011_rprest_lista': r5011_rprest_lista,    
            'r5011_rrecrepad_lista': r5011_rrecrepad_lista,    
            'r5011_rcoml_lista': r5011_rcoml_lista,    
            'r5011_rcprb_lista': r5011_rcprb_lista,
        }
        #return render(request, 'xml/%s/r5011_evttotalcontrib.html' % r5011_evttotalcontrib.versao, context, content_type='text/xml')
        t = get_template('%s/r5011_evttotalcontrib_xml.html' % r5011_evttotalcontrib.versao)
        xml = t.render(context)
        return xml
        

CERT_HOST = 'certificados/Kmee.pfx'
CERT_PASS = '58462273'
CERT_PEM_FILE = 'certificados/cert.pem'
KEY_PEM_FILE = 'certificados/key.pem'
CA_CERT_PEM_FILE = 'certificados/acserproacfv5.crt'

def recibo(request, hash, tipo, slug=0):
    from emensageriapro.efdreinf.models import r5001evtTotal, r5011evtTotalContrib
    from emensageriapro.r5001.models import r5001regOcorrs, r5001infoTotal, r5001RTom, \
        r5001infoCRTom, r5001RPrest, r5001RRecRepAD, r5001RComl, r5001RCPRB,r5001RRecEspetDesp
    from emensageriapro.r5011.models import r5011regOcorrs, r5011infoTotalContrib, r5011RTom, \
        r5011infoCRTom, r5011RPrest, r5011RRecRepAD, r5011RComl, r5011RCPRB
    
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    try: 
        usuario_id = request.session['usuario_id']   
        dict_hash = get_hash_url( hash )
        r5011_evttotalcontrib_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r5011_evttotalcontrib')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        
        r5011_evttotalcontrib = get_object_or_404(
            r5011evtTotalContrib.objects.using( db_slug ),
            excluido = False, id = r5011_evttotalcontrib_id)
    

        if r5011_evttotalcontrib.retornos_evttotal_id:

            r5001evtTotal_dados = get_object_or_404( r5001evtTotal.objects.using(db_slug),
                id=r5011_evttotalcontrib.retornos_evttotal_id, excluido=False)

            r5001infoTotal_dados = r5001infoTotal.objects.using(db_slug).\
                filter(r5001_evttotal_id=r5001evtTotal_dados.id,excluido=False).all()

            r5001RCPRB_dados = r5001RCPRB.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RComl_dados = r5001RComl.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RPrest_dados = r5001RPrest.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RRecEspetDesp_dados = r5001RRecEspetDesp.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RRecRepAD_dados = r5001RRecRepAD.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001RTom_dados = r5001RTom.objects.using(db_slug).\
                filter(r5001_infototal_id__in=listar_ids(r5001infoTotal_dados),excluido=False).all()

            r5001infoCRTom_dados = r5001infoCRTom.objects.using(db_slug).\
                filter(r5001_rtom_id__in=listar_ids(r5001RTom_dados),excluido=False).all()

            r5001regOcorrs_dados = r5001regOcorrs.objects.using(db_slug).\
                filter(r5001_evttotal_id=r5001evtTotal_dados.id,excluido=False).all()

        else:

            r5001evtTotal_dados = None

            r5001infoTotal_dados = None

            r5001RCPRB_dados = None

            r5001RComl_dados = None

            r5001RPrest_dados = None

            r5001RRecEspetDesp_dados = None

            r5001RRecRepAD_dados = None

            r5001RTom_dados = None

            r5001infoCRTom_dados = None

            r5001regOcorrs_dados = None

        if r5011_evttotalcontrib.retornos_evttotalcontrib_id:

            r5011evtTotalContrib_dados = get_object_or_404( r5011evtTotalContrib.objects.using(db_slug),
                id=r5011_evttotalcontrib.retornos_evttotalcontrib_id, excluido=False)

            r5011infoTotalContrib_dados = r5011infoTotalContrib.objects.using(db_slug).\
                filter(r5011_evttotalcontrib_id=r5011evtTotalContrib_dados.id,excluido=False).all()

            r5011RCPRB_dados = r5011RCPRB.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RComl_dados = r5011RComl.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RPrest_dados = r5011RPrest.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RRecEspetDesp_dados = None

            r5011RRecRepAD_dados = r5011RRecRepAD.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011RTom_dados = r5011RTom.objects.using(db_slug).\
                filter(r5011_infototalcontrib_id__in=listar_ids(r5011infoTotalContrib_dados),excluido=False).all()

            r5011infoCRTom_dados = r5011infoCRTom.objects.using(db_slug).\
                filter(r5011_rtom_id__in=listar_ids(r5011RTom_dados),excluido=False).all()

            r5011regOcorrs_dados = r5011regOcorrs.objects.using(db_slug).\
                filter(r5011_evttotalcontrib_id=r5011evtTotalContrib_dados.id,excluido=False).all()

        else:

            r5011evtTotalContrib_dados = None

            r5011infoTotalContrib_dados = None

            r5011RCPRB_dados = None

            r5011RComl_dados = None

            r5011RPrest_dados = None

            r5011RRecEspetDesp_dados = None

            r5011RRecRepAD_dados = None

            r5011RTom_dados = None

            r5011infoCRTom_dados = None

            r5011regOcorrs_dados = None



        
        context = {
            'r5011_evttotalcontrib_id': r5011_evttotalcontrib_id, 
            'r5011_evttotalcontrib': r5011_evttotalcontrib, 

            'r5001evtTotal_dados': r5001evtTotal_dados,
            'r5001infoTotal_dados': r5001infoTotal_dados,
            'r5001RCPRB_dados': r5001RCPRB_dados,
            'r5001RComl_dados': r5001RComl_dados,
            'r5001RPrest_dados': r5001RPrest_dados,
            'r5001RRecEspetDesp_dados': r5001RRecEspetDesp_dados,
            'r5001RRecRepAD_dados': r5001RRecRepAD_dados,
            'r5001RTom_dados': r5001RTom_dados,
            'r5001infoCRTom_dados': r5001infoCRTom_dados,
            'r5001regOcorrs_dados': r5001regOcorrs_dados,

            'r5011evtTotalContrib_dados': r5011evtTotalContrib_dados,
            'r5011infoTotalContrib_dados': r5011infoTotalContrib_dados,
            'r5011RCPRB_dados': r5011RCPRB_dados,
            'r5011RComl_dados': r5011RComl_dados,
            'r5011RPrest_dados': r5011RPrest_dados,
            'r5011RRecEspetDesp_dados': r5011RRecEspetDesp_dados,
            'r5011RRecRepAD_dados': r5011RRecRepAD_dados,
            'r5011RTom_dados': r5011RTom_dados,
            'r5011infoCRTom_dados': r5011infoCRTom_dados,
            'r5011regOcorrs_dados': r5011regOcorrs_dados,

            'conta': conta, 
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }
     

        if tipo == 'XLS':
            from django.shortcuts import render_to_response
            response =  render_to_response('r5011_evttotalcontrib_recibo_pdf.html', context)
            filename = "%s.xls" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif tipo == 'CSV':
            from django.shortcuts import render_to_response
            response =  render_to_response('r5011_evttotalcontrib_recibo_csv.html', context)
            filename = "%s.csv" % r5011_evttotalcontrib.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render_to_pdf('r5011_evttotalcontrib_recibo_pdf.html', context)
    else:
        context = {
            'usuario': usuario, 
            'conta': conta, 
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            'slug': slug,
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug):
    import os
    from datetime import datetime 
    from django.http import HttpResponse
    from emensageriapro.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import assinar_efdreinf
    r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False, id=r5011_evttotalcontrib_id)
    if r5011_evttotalcontrib.arquivo_original:
        xml = ler_arquivo(r5011_evttotalcontrib.arquivo)
    else:
        xml = gerar_xml_r5011(r5011_evttotalcontrib_id, db_slug)
    if 'Signature' in xml:
        xml_assinado = xml
    else:
        xml_assinado = assinar_efdreinf(xml)
    if r5011_evttotalcontrib.status in (0,1,2,11):
        r5011evtTotalContrib.objects.using(db_slug).filter(id=r5011_evttotalcontrib_id,excluido=False).update(status=10)
    arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % (r5011_evttotalcontrib.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r5011_evttotalcontrib/' % BASE_DIR)
    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_efdreinf(arquivo, xml_assinado, 1)
    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado


def gerar_xml(request, hash, slug=0):
    import os
    from datetime import datetime 
    from django.http import HttpResponse
    from emensageriapro.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import assinar_efdreinf
    hora_atual = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_') 
    for_print = 0
    if slug:
        conta = get_json(slug)
        if not conta:  
            raise Http404 
        else:
            db_slug = 'emensageriapro'+str(conta.id)
    else:
        db_slug = 'default'
        conta = None
    dict_hash = get_hash_url( hash )
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False, id=r5011_evttotalcontrib_id)
        xml_assinado = gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')
    else:
        context = {
            'conta': conta, 
            'slug': slug,
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



def duplicar(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False,
                                                    id=r5011_evttotalcontrib_id)

        arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug)
        
        texto = ler_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade)
        salvar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_duplicado_temp.xml' % r5011_evttotalcontrib.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_duplicado_temp.xml' % r5011_evttotalcontrib.identidade, request)
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r5011evtTotalContrib.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        messages.success(request, 'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r5011_evttotalcontrib.identidade), 
            'r5011_evttotalcontrib', dados['identidade'], usuario_id, 1)
        return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)
    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def criar_alteracao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False,
                                                    id=r5011_evttotalcontrib_id)
        arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade)
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        salvar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_alteracao_temp.xml' % r5011_evttotalcontrib.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_alteracao_temp.xml' % r5011_evttotalcontrib.identidade, request)
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r5011evtTotalContrib.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r5011_evttotalcontrib.identidade), 
            'r5011_evttotalcontrib', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




def criar_exclusao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False,
                                                    id=r5011_evttotalcontrib_id)
        arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % r5011_evttotalcontrib.identidade)
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        salvar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_exclusao_temp.xml' % r5011_evttotalcontrib.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/r5011_evttotalcontrib/%s_exclusao_temp.xml' % r5011_evttotalcontrib.identidade, request)
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        r5011evtTotalContrib.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (dent, r5011_evttotalcontrib.identidade), 
            'r5011_evttotalcontrib', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])





def alterar_identidade(request, hash):
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False,
                                                    id=r5011_evttotalcontrib_id)
        if r5011_evttotalcontrib.status == 0:
            from emensageriapro.efdreinf.views.r5011_evttotalcontrib import identidade_evento
            dent = identidade_evento(r5011_evttotalcontrib_id, db_slug)
            messages.success(request, 'Identidade do evento alterada com sucesso!')
            usuario_id = request.session['usuario_id'] 
            gravar_auditoria(u'{}', u'{"funcao": "Identidade do evento foi alterada"}', 
            'r5011_evttotalcontrib', r5011_evttotalcontrib_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % r5011_evttotalcontrib_id )
            return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)
        else:
            messages.error(request, 'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_efdreinf import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False, id=r5011_evttotalcontrib_id)
        if r5011_evttotalcontrib.status in (0, 1, 2, 3, 4, 5, 10, 11):
            r5011evtTotalContrib.objects.using(db_slug).filter(id=r5011_evttotalcontrib_id).update(status=0, arquivo_original=0)
            arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % (r5011_evttotalcontrib.identidade)
            if os.path.exists(BASE_DIR + '/' + arquivo):
                from datetime import datetime
                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, r5011_evttotalcontrib.identidade, BASE_DIR, r5011_evttotalcontrib.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/r5011_evttotalcontrib/%s.xml %s/arquivos/Eventos/r5011_evttotalcontrib/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/r5011_evttotalcontrib/%s_backup_%s.xml' % (r5011_evttotalcontrib.identidade, data_hora_atual), 
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.session['usuario_id'] 
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}', 
            'r5011_evttotalcontrib', r5011_evttotalcontrib_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % r5011_evttotalcontrib_id )
            return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)
        else:
            messages.error(request, '''
            Não foi possível abrir o evento para edição! Somente é possível 
            abrir eventos com os seguintes status: "Cadastrado", "Importado", "Validado", 
            "Duplicado", "Erro na validação", "XML Assinado" ou "XML Gerado"
             ou com o status "Enviado com sucesso" e os seguintes códigos de resposta do servidor:
             "401 - Lote Incorreto - Erro preenchimento" ou "402 - Lote Incorreto - schema Inválido"!''')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao abrir evento para edição!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def validar_evento_funcao(r5011_evttotalcontrib_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.funcoes_importacao import get_versao_evento
    from emensageriapro.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    lista_validacoes = []
    r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False, id=r5011_evttotalcontrib_id)
    quant = validar_precedencia('efdreinf', 'r5011_evttotalcontrib', r5011_evttotalcontrib_id)
    if quant <= 0:
        lista_validacoes.append('Precedência não foi enviada!')
        precedencia = 0
    else:
        precedencia = 1
    executar_sql("UPDATE public.r5011_evttotalcontrib SET validacao_precedencia=%s WHERE id=%s;" % (precedencia, r5011_evttotalcontrib_id), False)
    #
    # Validações internas
    #
    arquivo = 'arquivos/Eventos/r5011_evttotalcontrib/%s.xml' % (r5011_evttotalcontrib.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r5011_evttotalcontrib/' % BASE_DIR)
    lista = []
    tipo = 'efdreinf'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(r5011_evttotalcontrib_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        if tipo == 'esocial':
            if versao == 'v02_04_02':
                from emensageriapro.esocial.validacoes.v02_04_02.r5011_evttotalcontrib import validacoes_r5011_evttotalcontrib
                lista = validacoes_r5011_evttotalcontrib(arquivo)
        elif tipo == 'efdreinf':
            if versao == 'v1_03_02':
                from emensageriapro.efdreinf.validacoes.v1_03_02.r5011_evttotalcontrib import validacoes_r5011_evttotalcontrib
                lista = validacoes_r5011_evttotalcontrib(arquivo)
    for a in lista:
        if a:
            lista_validacoes.append(a)
    #
    # validando schema
    #
    schema_filename = get_schema_name(arquivo)
    quant_erros, error_list = validar_schema(schema_filename, arquivo, lang='pt')
    for a in error_list:
        if a:
            lista_validacoes.append(a)
    #
    #
    #
    if lista_validacoes:
        executar_sql("UPDATE public.r5011_evttotalcontrib SET validacoes='%s', status=3 WHERE id=%s;" % ('<br>'.join(lista_validacoes).replace("'","''"), r5011_evttotalcontrib_id), False)
    else:
        executar_sql("UPDATE public.r5011_evttotalcontrib SET validacoes='', status=4 WHERE id=%s;" % (r5011_evttotalcontrib_id), False)
    return lista_validacoes



def validar_evento(request, hash):
    from emensageriapro.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    r5011_evttotalcontrib_id = int(dict_hash['id'])
    if r5011_evttotalcontrib_id:
        lista_validacoes = []
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib.objects.using(db_slug), excluido=False, id=r5011_evttotalcontrib_id)
        if r5011_evttotalcontrib.versao in VERSAO_ATUAL:
            lista_validacoes = validar_evento_funcao(r5011_evttotalcontrib_id, db_slug)
            messages.success(request, 'Validações processadas com sucesso!')
        else:
            messages.error(request, 'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:    
        messages.error(request, 'Não foi possível validar o evento pois o mesmo não foi identificado!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])