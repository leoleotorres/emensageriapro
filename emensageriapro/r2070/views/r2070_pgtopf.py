#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.r2070.forms import *
from emensageriapro.r2070.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2070_pgtopf_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_pgtopf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r2070_pgtopf_id:
        r2070_pgtopf = get_object_or_404(r2070pgtoPF.objects.using( db_slug ), excluido = False, id = r2070_pgtopf_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r2070_pgtopf_id:
        dados_evento = r2070_pgtopf.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2070_pgtopf_apagar'] = 0
            dict_permissoes['r2070_pgtopf_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2070_pgtopf_id:
            r2070_pgtopf_form = form_r2070_pgtopf(request.POST or None, instance = r2070_pgtopf, slug = db_slug)
        else:
            r2070_pgtopf_form = form_r2070_pgtopf(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r2070_pgtopf_form.is_valid():
                dados = r2070_pgtopf_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r2070_pgtopf_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r2070_pgtopf_campos_multiple_passo1
                        r2070pgtoPF.objects.using(db_slug).filter(id=r2070_pgtopf_id).update(**dados)
                        obj = r2070pgtoPF.objects.using(db_slug).get(id=r2070_pgtopf_id)
                        #r2070_pgtopf_editar_custom
                        #r2070_pgtopf_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r2070_pgtopf), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r2070_pgtopf', r2070_pgtopf_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r2070_pgtopf_cadastrar_campos_multiple_passo1
                    obj = r2070pgtoPF(**dados)
                    obj.save(using = db_slug)
                    #r2070_pgtopf_cadastrar_custom
                    #r2070_pgtopf_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2070_pgtopf', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('r2070_pgtopf_apagar', 'r2070_pgtopf_salvar', 'r2070_pgtopf'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if r2070_pgtopf_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('r2070_pgtopf_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r2070_pgtopf_form = disabled_form_fields(r2070_pgtopf_form, permissao.permite_editar)
        if r2070_pgtopf_id:
            if dados_evento['status'] != 0:
                r2070_pgtopf_form = disabled_form_fields(r2070_pgtopf_form, 0)
        #r2070_pgtopf_campos_multiple_passo3

        for field in r2070_pgtopf_form.fields.keys():
            r2070_pgtopf_form.fields[field].widget.attrs['ng-model'] = 'r2070_pgtopf_'+field
        if int(dict_hash['print']):
            r2070_pgtopf_form = disabled_form_for_print(r2070_pgtopf_form)

        r2070_detdeducao_form = None
        r2070_detdeducao_lista = None
        r2070_rendisento_form = None
        r2070_rendisento_lista = None
        r2070_detcompet_form = None
        r2070_detcompet_lista = None
        r2070_compjud_form = None
        r2070_compjud_lista = None
        r2070_inforra_form = None
        r2070_inforra_lista = None
        r2070_infoprocjud_form = None
        r2070_infoprocjud_lista = None
        r2070_depjudicial_form = None
        r2070_depjudicial_lista = None
        if r2070_pgtopf_id:
            r2070_pgtopf = get_object_or_404(r2070pgtoPF.objects.using( db_slug ), excluido = False, id = r2070_pgtopf_id)
  
            r2070_detdeducao_form = form_r2070_detdeducao(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_detdeducao_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_detdeducao_lista = r2070detDeducao.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_rendisento_form = form_r2070_rendisento(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_rendisento_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_rendisento_lista = r2070rendIsento.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_detcompet_form = form_r2070_detcompet(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_detcompet_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_detcompet_lista = r2070detCompet.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_compjud_form = form_r2070_compjud(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_compjud_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_compjud_lista = r2070compJud.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_inforra_form = form_r2070_inforra(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_inforra_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_inforra_lista = r2070infoRRA.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_infoprocjud_form = form_r2070_infoprocjud(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_infoprocjud_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_infoprocjud_lista = r2070infoProcJud.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
            r2070_depjudicial_form = form_r2070_depjudicial(initial={ 'r2070_pgtopf': r2070_pgtopf }, slug=db_slug)
            r2070_depjudicial_form.fields['r2070_pgtopf'].widget.attrs['readonly'] = True
            r2070_depjudicial_lista = r2070depJudicial.objects.using( db_slug ).filter(excluido = False, r2070_pgtopf_id=r2070_pgtopf.id).all()
        else:
            r2070_pgtopf = None
        #r2070_pgtopf_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r2070_pgtopf' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2070_pgtopf_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2070_pgtopf_id, tabela='r2070_pgtopf').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r2070_pgtopf': r2070_pgtopf,
            'r2070_pgtopf_form': r2070_pgtopf_form,
            'mensagem': mensagem,
            'r2070_pgtopf_id': int(r2070_pgtopf_id),
            'usuario': usuario,
       
            'hash': hash,
  
            'r2070_detdeducao_form': r2070_detdeducao_form,
            'r2070_detdeducao_lista': r2070_detdeducao_lista,
            'r2070_rendisento_form': r2070_rendisento_form,
            'r2070_rendisento_lista': r2070_rendisento_lista,
            'r2070_detcompet_form': r2070_detcompet_form,
            'r2070_detcompet_lista': r2070_detcompet_lista,
            'r2070_compjud_form': r2070_compjud_form,
            'r2070_compjud_lista': r2070_compjud_lista,
            'r2070_inforra_form': r2070_inforra_form,
            'r2070_inforra_lista': r2070_inforra_lista,
            'r2070_infoprocjud_form': r2070_infoprocjud_form,
            'r2070_infoprocjud_lista': r2070_infoprocjud_lista,
            'r2070_depjudicial_form': r2070_depjudicial_form,
            'r2070_depjudicial_lista': r2070_depjudicial_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2070_pgtopf_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'r2070_pgtopf_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2070_pgtopf_salvar.html',
                filename="r2070_pgtopf.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('r2070_pgtopf_salvar.html', context)
            filename = "r2070_pgtopf.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2070_pgtopf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_pgtopf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r2070_pgtopf = get_object_or_404(r2070pgtoPF.objects.using( db_slug ), excluido = False, id = r2070_pgtopf_id)
    dados_evento = {}
    if r2070_pgtopf_id:
        dados_evento = r2070_pgtopf.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2070_pgtopf_apagar'] = 0
            dict_permissoes['r2070_pgtopf_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2070_pgtopf), indent=4, sort_keys=True, default=str)
            r2070pgtoPF.objects.using( db_slug ).filter(id = r2070_pgtopf_id).delete()
            #r2070_pgtopf_apagar_custom
            #r2070_pgtopf_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2070_pgtopf', r2070_pgtopf_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
   
        if request.session['retorno_pagina']== 'r2070_pgtopf_salvar':
            return redirect('r2070_pgtopf', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,
   
        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,
   
        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'r2070_pgtopf_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class r2070pgtoPFList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r2070pgtoPF.objects.using(db_slug).all()
    serializer_class = r2070pgtoPFSerializer
    permission_classes = (IsAdminUser,)


class r2070pgtoPFDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r2070pgtoPF.objects.using(db_slug).all()
    serializer_class = r2070pgtoPFSerializer
    permission_classes = (IsAdminUser,)


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


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r2070_pgtopf_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2070_pgtopf')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_vlrirrf': 1,
            'show_vlrrendtributavel': 1,
            'show_inddecterceiro': 1,
            'show_indsuspexig': 1,
            'show_dtpgto': 1,
            'show_r2070_pgtoresidbr': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'vlrirrf': 'vlrirrf',
                'vlrrendtributavel': 'vlrrendtributavel',
                'inddecterceiro__icontains': 'inddecterceiro__icontains',
                'indsuspexig__icontains': 'indsuspexig__icontains',
                'dtpgto__range': 'dtpgto__range',
                'r2070_pgtoresidbr': 'r2070_pgtoresidbr',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'vlrirrf': 'vlrirrf',
                'vlrrendtributavel': 'vlrrendtributavel',
                'inddecterceiro__icontains': 'inddecterceiro__icontains',
                'indsuspexig__icontains': 'indsuspexig__icontains',
                'dtpgto__range': 'dtpgto__range',
                'r2070_pgtoresidbr': 'r2070_pgtoresidbr',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2070_pgtopf_lista = r2070pgtoPF.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2070_pgtopf_lista) > 100:
            filtrar = True
            r2070_pgtopf_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r2070_pgtopf_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2070_pgtopf'
        context = {
            'r2070_pgtopf_lista': r2070_pgtopf_lista,
       
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,
   
        }
        if for_print in (0,1):
            return render(request, 'r2070_pgtopf_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2070_pgtopf_listar.html',
                filename="r2070_pgtopf.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('r2070_pgtopf_listar.html', context)
            filename = "r2070_pgtopf.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r2070_pgtopf_csv.html', context)
            filename = "r2070_pgtopf.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
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

