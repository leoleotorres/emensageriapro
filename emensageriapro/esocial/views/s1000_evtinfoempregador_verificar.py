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
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64
from emensageriapro.s1000.models import *
from emensageriapro.s1000.forms import *
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



def verificar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1000_evtinfoempregador_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_evtinfoempregador')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using( db_slug ), excluido = False, id = s1000_evtinfoempregador_id)
        s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects.using( db_slug ).filter(id=s1000_evtinfoempregador_id, excluido = False).all()
   

        s1000_inclusao_lista = s1000inclusao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        s1000_inclusao_dadosisencao_lista = s1000inclusaodadosIsencao.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoop_lista = s1000inclusaoinfoOP.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoefr_lista = s1000inclusaoinfoEFR.objects.using(db_slug).filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoente_lista = s1000inclusaoinfoEnte.objects.using(db_slug).filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoorginternacional_lista = s1000inclusaoinfoOrgInternacional.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_softwarehouse_lista = s1000inclusaosoftwareHouse.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_situacaopj_lista = s1000inclusaosituacaoPJ.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_situacaopf_lista = s1000inclusaosituacaoPF.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_alteracao_lista = s1000alteracao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        s1000_alteracao_dadosisencao_lista = s1000alteracaodadosIsencao.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoop_lista = s1000alteracaoinfoOP.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoefr_lista = s1000alteracaoinfoEFR.objects.using(db_slug).filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoente_lista = s1000alteracaoinfoEnte.objects.using(db_slug).filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoorginternacional_lista = s1000alteracaoinfoOrgInternacional.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_softwarehouse_lista = s1000alteracaosoftwareHouse.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_situacaopj_lista = s1000alteracaosituacaoPJ.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_situacaopf_lista = s1000alteracaosituacaoPF.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_novavalidade_lista = s1000alteracaonovaValidade.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_exclusao_lista = s1000exclusao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1000_evtinfoempregador'
        context = {
            's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,
            's1000_evtinfoempregador_id': s1000_evtinfoempregador_id,
            's1000_evtinfoempregador': s1000_evtinfoempregador,
            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,

            's1000_inclusao_lista': s1000_inclusao_lista,
            's1000_inclusao_dadosisencao_lista': s1000_inclusao_dadosisencao_lista,
            's1000_inclusao_infoop_lista': s1000_inclusao_infoop_lista,
            's1000_inclusao_infoefr_lista': s1000_inclusao_infoefr_lista,
            's1000_inclusao_infoente_lista': s1000_inclusao_infoente_lista,
            's1000_inclusao_infoorginternacional_lista': s1000_inclusao_infoorginternacional_lista,
            's1000_inclusao_softwarehouse_lista': s1000_inclusao_softwarehouse_lista,
            's1000_inclusao_situacaopj_lista': s1000_inclusao_situacaopj_lista,
            's1000_inclusao_situacaopf_lista': s1000_inclusao_situacaopf_lista,
            's1000_alteracao_lista': s1000_alteracao_lista,
            's1000_alteracao_dadosisencao_lista': s1000_alteracao_dadosisencao_lista,
            's1000_alteracao_infoop_lista': s1000_alteracao_infoop_lista,
            's1000_alteracao_infoefr_lista': s1000_alteracao_infoefr_lista,
            's1000_alteracao_infoente_lista': s1000_alteracao_infoente_lista,
            's1000_alteracao_infoorginternacional_lista': s1000_alteracao_infoorginternacional_lista,
            's1000_alteracao_softwarehouse_lista': s1000_alteracao_softwarehouse_lista,
            's1000_alteracao_situacaopj_lista': s1000_alteracao_situacaopj_lista,
            's1000_alteracao_situacaopf_lista': s1000_alteracao_situacaopf_lista,
            's1000_alteracao_novavalidade_lista': s1000_alteracao_novavalidade_lista,
            's1000_exclusao_lista': s1000_exclusao_lista,
        }
        if for_print == 2:
            #return render_to_pdf('%s/s1000_evtinfoempregador_verificar.html' % s1000_evtinfoempregador.versao, context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(request=request,
                                           template='%s/s1000_evtinfoempregador_verificar.html' % s1000_evtinfoempregador.versao,
                                           filename="s1000_evtinfoempregador.pdf",
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
            response =  render_to_response('%s/s1000_evtinfoempregador_verificar.html' % s1000_evtinfoempregador.versao, context)
            filename = "%s.xls" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response =  render_to_response('%s/s1000_evtinfoempregador_verificar.html' % s1000_evtinfoempregador.versao, context)
            filename = "%s.csv" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render(request, '%s/s1000_evtinfoempregador_verificar.html' % s1000_evtinfoempregador.versao, context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_s1000(s1000_evtinfoempregador_id, db_slug):
    from django.template.loader import get_template
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using( db_slug ), excluido = False, id = s1000_evtinfoempregador_id)
        s1000_evtinfoempregador_lista = s1000evtInfoEmpregador.objects.using( db_slug ).filter(id=s1000_evtinfoempregador_id, excluido = False).all()

        s1000_inclusao_lista = s1000inclusao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        s1000_inclusao_dadosisencao_lista = s1000inclusaodadosIsencao.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoop_lista = s1000inclusaoinfoOP.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoefr_lista = s1000inclusaoinfoEFR.objects.using(db_slug).filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoente_lista = s1000inclusaoinfoEnte.objects.using(db_slug).filter(s1000_inclusao_infoop_id__in = listar_ids(s1000_inclusao_infoop_lista) ).filter(excluido=False).all()
        s1000_inclusao_infoorginternacional_lista = s1000inclusaoinfoOrgInternacional.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_softwarehouse_lista = s1000inclusaosoftwareHouse.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_situacaopj_lista = s1000inclusaosituacaoPJ.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_inclusao_situacaopf_lista = s1000inclusaosituacaoPF.objects.using(db_slug).filter(s1000_inclusao_id__in = listar_ids(s1000_inclusao_lista) ).filter(excluido=False).all()
        s1000_alteracao_lista = s1000alteracao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        s1000_alteracao_dadosisencao_lista = s1000alteracaodadosIsencao.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoop_lista = s1000alteracaoinfoOP.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoefr_lista = s1000alteracaoinfoEFR.objects.using(db_slug).filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoente_lista = s1000alteracaoinfoEnte.objects.using(db_slug).filter(s1000_alteracao_infoop_id__in = listar_ids(s1000_alteracao_infoop_lista) ).filter(excluido=False).all()
        s1000_alteracao_infoorginternacional_lista = s1000alteracaoinfoOrgInternacional.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_softwarehouse_lista = s1000alteracaosoftwareHouse.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_situacaopj_lista = s1000alteracaosituacaoPJ.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_situacaopf_lista = s1000alteracaosituacaoPF.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_alteracao_novavalidade_lista = s1000alteracaonovaValidade.objects.using(db_slug).filter(s1000_alteracao_id__in = listar_ids(s1000_alteracao_lista) ).filter(excluido=False).all()
        s1000_exclusao_lista = s1000exclusao.objects.using(db_slug).filter(s1000_evtinfoempregador_id__in = listar_ids(s1000_evtinfoempregador_lista) ).filter(excluido=False).all()
        context = {
            'base': s1000_evtinfoempregador,
            's1000_evtinfoempregador_lista': s1000_evtinfoempregador_lista,
            's1000_evtinfoempregador_id': int(s1000_evtinfoempregador_id),
            's1000_evtinfoempregador': s1000_evtinfoempregador,

            's1000_inclusao_lista': s1000_inclusao_lista,
            's1000_inclusao_dadosisencao_lista': s1000_inclusao_dadosisencao_lista,
            's1000_inclusao_infoop_lista': s1000_inclusao_infoop_lista,
            's1000_inclusao_infoefr_lista': s1000_inclusao_infoefr_lista,
            's1000_inclusao_infoente_lista': s1000_inclusao_infoente_lista,
            's1000_inclusao_infoorginternacional_lista': s1000_inclusao_infoorginternacional_lista,
            's1000_inclusao_softwarehouse_lista': s1000_inclusao_softwarehouse_lista,
            's1000_inclusao_situacaopj_lista': s1000_inclusao_situacaopj_lista,
            's1000_inclusao_situacaopf_lista': s1000_inclusao_situacaopf_lista,
            's1000_alteracao_lista': s1000_alteracao_lista,
            's1000_alteracao_dadosisencao_lista': s1000_alteracao_dadosisencao_lista,
            's1000_alteracao_infoop_lista': s1000_alteracao_infoop_lista,
            's1000_alteracao_infoefr_lista': s1000_alteracao_infoefr_lista,
            's1000_alteracao_infoente_lista': s1000_alteracao_infoente_lista,
            's1000_alteracao_infoorginternacional_lista': s1000_alteracao_infoorginternacional_lista,
            's1000_alteracao_softwarehouse_lista': s1000_alteracao_softwarehouse_lista,
            's1000_alteracao_situacaopj_lista': s1000_alteracao_situacaopj_lista,
            's1000_alteracao_situacaopf_lista': s1000_alteracao_situacaopf_lista,
            's1000_alteracao_novavalidade_lista': s1000_alteracao_novavalidade_lista,
            's1000_exclusao_lista': s1000_exclusao_lista,
        }
        #return render(request, 'xml/%s/s1000_evtinfoempregador.html' % s1000_evtinfoempregador.versao, context, content_type='text/xml')
        t = get_template('%s/s1000_evtinfoempregador_xml.html' % s1000_evtinfoempregador.versao)
        xml = t.render(context)
        return xml
   



def recibo(request, hash, tipo):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1000_evtinfoempregador_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1000_evtinfoempregador')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
   
        s1000_evtinfoempregador = get_object_or_404(
            s1000evtInfoEmpregador.objects.using( db_slug ),
            excluido = False, id = s1000_evtinfoempregador_id)

        from emensageriapro.mensageiro.models import RetornosEventos, RetornosEventosHorarios, \
            RetornosEventosIntervalos, RetornosEventosOcorrencias

        retorno = get_object_or_404( RetornosEventos.objects.using(db_slug),
            id=s1000_evtinfoempregador.retornos_eventos_id, excluido=False)

        retorno_horarios = RetornosEventosHorarios.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()

        retorno_intervalos = RetornosEventosIntervalos.objects.using(db_slug).\
            filter(retornos_eventos_horarios_id__in=listar_ids(retorno_horarios),excluido=False).all()

        retorno_ocorrencias = RetornosEventosOcorrencias.objects.using(db_slug).\
            filter(retornos_eventos_id=retorno.id,excluido=False).all()
   
        context = {
            's1000_evtinfoempregador_id': s1000_evtinfoempregador_id,
            's1000_evtinfoempregador': s1000_evtinfoempregador,

            'retorno': retorno,
            'retorno_horarios': retorno_horarios,
            'retorno_intervalos': retorno_intervalos,
            'retorno_ocorrencias': retorno_ocorrencias,

            
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': for_print,
            'hash': hash,
        }

        if tipo == 'XLS':
            from django.shortcuts import render_to_response
            response =  render_to_response('s1000_evtinfoempregador_recibo_pdf.html', context)
            filename = "%s.xls" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif tipo == 'CSV':
            from django.shortcuts import render_to_response
            response =  render_to_response('s1000_evtinfoempregador_recibo_csv.html', context)
            filename = "%s.csv" % s1000_evtinfoempregador.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
        else:
            return render_to_pdf('s1000_evtinfoempregador_recibo_pdf.html', context)
    else:
        context = {
            'usuario': usuario,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
            
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)



def gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug):
    import os
    from datetime import datetime
    from django.http import HttpResponse
    from emensageriapro.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import assinar_esocial
    s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False, id=s1000_evtinfoempregador_id)
    if s1000_evtinfoempregador.arquivo_original:
        xml = ler_arquivo(s1000_evtinfoempregador.arquivo)
    else:
        xml = gerar_xml_s1000(s1000_evtinfoempregador_id, db_slug)
    if 'Signature' in xml:
        xml_assinado = xml
    else:
        xml_assinado = assinar_esocial(xml)
    if s1000_evtinfoempregador.status in (0,1,2,11):
        s1000evtInfoEmpregador.objects.using(db_slug).filter(id=s1000_evtinfoempregador_id,excluido=False).update(status=10)
    arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % (s1000_evtinfoempregador.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1000_evtinfoempregador/' % BASE_DIR)
    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_esocial(arquivo, xml_assinado, 1)
    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado


def gerar_xml(request, hash):
    import os
    from datetime import datetime
    from django.http import HttpResponse
    from emensageriapro.funcoes_esocial import salvar_arquivo_esocial
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import assinar_esocial
    hora_atual = str(datetime.now()).replace(' ', '_').replace('.', '_').replace(':', '_')
    for_print = 0
    db_slug = 'default'
    dict_hash = get_hash_url( hash )
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False, id=s1000_evtinfoempregador_id)
        xml_assinado = gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug)
        return HttpResponse(xml_assinado, content_type='text/xml')
    else:
        context = {
            
            
            'data': datetime.datetime.now(),
        }
        return render(request, 'permissao_negada.html', context)



def duplicar(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False,
                                                    id=s1000_evtinfoempregador_id)

        arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug)
   
        texto = ler_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade)
        salvar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_duplicado_temp.xml' % s1000_evtinfoempregador.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_duplicado_temp.xml' % s1000_evtinfoempregador.identidade, request)
        from emensageriapro.esocial.views.s1000_evtinfoempregador import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s1000evtInfoEmpregador.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        messages.success(request, 'Evento duplicado com sucesso! Foi criado uma nova identidade para este evento!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s1000_evtinfoempregador.identidade),
            's1000_evtinfoempregador', dados['identidade'], usuario_id, 1)
        return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)
    messages.error(request, 'Erro ao duplicar evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def criar_alteracao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False,
                                                    id=s1000_evtinfoempregador_id)
        arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade)
        texto = texto.replace('<inclusao>','<alteracao>').replace('</inclusao>','</alteracao>')
        salvar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_alteracao_temp.xml' % s1000_evtinfoempregador.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_alteracao_temp.xml' % s1000_evtinfoempregador.identidade, request)
        from emensageriapro.esocial.views.s1000_evtinfoempregador import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s1000evtInfoEmpregador.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de de alteração de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s1000_evtinfoempregador.identidade),
            's1000_evtinfoempregador', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de alteração criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de alteração!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])




def criar_exclusao(request, hash):
    from emensageriapro.settings import BASE_DIR
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False,
                                                    id=s1000_evtinfoempregador_id)
        arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade
        if not os.path.exists(BASE_DIR + '/' + arquivo):
            xml = gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug)
        texto = ler_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % s1000_evtinfoempregador.identidade)
        texto = texto.replace('<inclusao>','<exclusao>').replace('</inclusao>','</exclusao>')
        texto = texto.replace('<alteracao>','<exclusao>').replace('</alteracao>','</exclusao>')
        salvar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_exclusao_temp.xml' % s1000_evtinfoempregador.identidade, texto)
        from emensageriapro.funcoes_importacao import importar_arquivo
        dados = importar_arquivo('arquivos/Eventos/s1000_evtinfoempregador/%s_exclusao_temp.xml' % s1000_evtinfoempregador.identidade, request)
        from emensageriapro.esocial.views.s1000_evtinfoempregador import identidade_evento
        dent = identidade_evento(dados['identidade'], db_slug)
        s1000evtInfoEmpregador.objects.using(db_slug).filter(id=dados['identidade']).update(status=0, arquivo_original=0, arquivo='')
        usuario_id = request.session['usuario_id']
        gravar_auditoria(u'{}', u'{"funcao": "Evento de exclusão de identidade %s criado a partir da duplicação do evento %s"}' % (dent, s1000_evtinfoempregador.identidade),
            's1000_evtinfoempregador', dados['identidade'], usuario_id, 1)
        messages.success(request, 'Evento de exclusão criado com sucesso!')
        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % dados['identidade'] )
        return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)
    messages.error(request, 'Erro ao criar evento de exclusão!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])





def alterar_identidade(request, hash):
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False,
                                                    id=s1000_evtinfoempregador_id)
        if s1000_evtinfoempregador.status == 0:
            from emensageriapro.esocial.views.s1000_evtinfoempregador import identidade_evento
            dent = identidade_evento(s1000_evtinfoempregador_id, db_slug)
            messages.success(request, 'Identidade do evento alterada com sucesso!')
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s1000_evtinfoempregador_id )
            usuario_id = request.session['usuario_id']
            gravar_auditoria(u'{}', u'{"funcao": "Identidade do evento foi alterada"}',
            's1000_evtinfoempregador', s1000_evtinfoempregador_id, usuario_id, 1)
            return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)
        else:
            messages.error(request, 'Não foi possível alterar a identidade do evento! Somente é possível alterar o status de eventos que estão abertos para edição (status: Cadastrado)!')
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])

    messages.error(request, 'Erro ao alterar identidade do evento!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])



def abrir_evento_para_edicao(request, hash):
    from emensageriapro.settings import BASE_DIR
    from emensageriapro.funcoes_esocial import gravar_nome_arquivo
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False, id=s1000_evtinfoempregador_id)
        if s1000_evtinfoempregador.status in (0, 1, 2, 3, 4, 10, 11) or s1000_evtinfoempregador.processamento_codigo_resposta in (401,402):
            s1000evtInfoEmpregador.objects.using(db_slug).filter(id=s1000_evtinfoempregador_id).update(status=0, arquivo_original=0)
            arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % (s1000_evtinfoempregador.identidade)
            if os.path.exists(BASE_DIR + '/' + arquivo):
                from datetime import datetime
                data_hora_atual = str(datetime.now()).replace(':','_').replace(' ','_').replace('.','_')
                dad = (BASE_DIR, s1000_evtinfoempregador.identidade, BASE_DIR, s1000_evtinfoempregador.identidade, data_hora_atual)
                os.system('mv %s/arquivos/Eventos/s1000_evtinfoempregador/%s.xml %s/arquivos/Eventos/s1000_evtinfoempregador/%s_backup_%s.xml' % dad)
                gravar_nome_arquivo('/arquivos/Eventos/s1000_evtinfoempregador/%s_backup_%s.xml' % (s1000_evtinfoempregador.identidade, data_hora_atual),
                    1)
            messages.success(request, 'Evento aberto para edição!')
            usuario_id = request.session['usuario_id']
            gravar_auditoria(u'{}', u'{"funcao": "Evento aberto para edição"}',
            's1000_evtinfoempregador', s1000_evtinfoempregador_id, usuario_id, 1)
            url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % s1000_evtinfoempregador_id )
            return redirect('s1000_evtinfoempregador_salvar', hash=url_hash)
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



def validar_evento_funcao(s1000_evtinfoempregador_id, db_slug):
    from emensageriapro.padrao import executar_sql
    from emensageriapro.funcoes_importacao import get_versao_evento
    from emensageriapro.funcoes_validacoes_precedencia import validar_precedencia
    from emensageriapro.funcoes_validacoes import get_schema_name, validar_schema
    from emensageriapro.settings import BASE_DIR
    lista_validacoes = []
    s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False, id=s1000_evtinfoempregador_id)
    quant = validar_precedencia('esocial', 's1000_evtinfoempregador', s1000_evtinfoempregador_id)
    if quant <= 0:
        #lista_validacoes.append('Precedência não foi enviada!')
        precedencia = 0
    else:
        precedencia = 1
    executar_sql("UPDATE public.s1000_evtinfoempregador SET validacao_precedencia=%s WHERE id=%s;" % (precedencia, s1000_evtinfoempregador_id), False)
    #
    # Validações internas
    #
    arquivo = 'arquivos/Eventos/s1000_evtinfoempregador/%s.xml' % (s1000_evtinfoempregador.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/s1000_evtinfoempregador/' % BASE_DIR)
    lista = []
    tipo = 'esocial'
    if not os.path.exists(BASE_DIR + '/' + arquivo):
        gerar_xml_assinado(s1000_evtinfoempregador_id, db_slug)
    if os.path.exists(BASE_DIR + '/' + arquivo):
        texto_xml = ler_arquivo(arquivo).replace("s:", "")
        versao = get_versao_evento(texto_xml)
        if tipo == 'esocial':
            if versao == 'v02_04_02':
                from emensageriapro.esocial.validacoes.v02_04_02.s1000_evtinfoempregador import validacoes_s1000_evtinfoempregador
                lista = validacoes_s1000_evtinfoempregador(arquivo)
        elif tipo == 'efdreinf':
            if versao == 'v1_03_02':
                from emensageriapro.efdreinf.validacoes.v1_03_02.s1000_evtinfoempregador import validacoes_s1000_evtinfoempregador
                lista = validacoes_s1000_evtinfoempregador(arquivo)
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
        executar_sql("UPDATE public.s1000_evtinfoempregador SET validacoes='%s', status=3 WHERE id=%s;" % ('<br>'.join(lista_validacoes).replace("'","''"), s1000_evtinfoempregador_id), False)
    else:
        executar_sql("UPDATE public.s1000_evtinfoempregador SET validacoes='', status=4 WHERE id=%s;" % (s1000_evtinfoempregador_id), False)
    return lista_validacoes



def validar_evento(request, hash):
    from emensageriapro.funcoes_validacoes import VERSAO_ATUAL
    db_slug = 'default'
    dict_hash = get_hash_url(hash)
    s1000_evtinfoempregador_id = int(dict_hash['id'])
    if s1000_evtinfoempregador_id:
        lista_validacoes = []
        s1000_evtinfoempregador = get_object_or_404(s1000evtInfoEmpregador.objects.using(db_slug), excluido=False, id=s1000_evtinfoempregador_id)
        if s1000_evtinfoempregador.versao in VERSAO_ATUAL:
            lista_validacoes = validar_evento_funcao(s1000_evtinfoempregador_id, db_slug)
            messages.success(request, 'Validações processadas com sucesso!')
        else:
            messages.error(request, 'Não foi possível validar o evento pois a versão do evento não é compatível com a versão do sistema!')
    else:
        messages.error(request, 'Não foi possível validar o evento pois o mesmo não foi identificado!')
    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])