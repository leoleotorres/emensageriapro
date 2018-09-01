#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.s1210.forms import *
from emensageriapro.s1210.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1210_detpgtoant_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1210_detpgtoant')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1210_detpgtoant_id:
        s1210_detpgtoant = get_object_or_404(s1210detPgtoAnt.objects.using( db_slug ), excluido = False, id = s1210_detpgtoant_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if s1210_detpgtoant_id:
        dados_evento = s1210_detpgtoant.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1210_detpgtoant_apagar'] = 0
            dict_permissoes['s1210_detpgtoant_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1210_detpgtoant_id:
            s1210_detpgtoant_form = form_s1210_detpgtoant(request.POST or None, instance = s1210_detpgtoant, slug = db_slug)
        else:
            s1210_detpgtoant_form = form_s1210_detpgtoant(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if s1210_detpgtoant_form.is_valid():
                dados = s1210_detpgtoant_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if s1210_detpgtoant_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #s1210_detpgtoant_campos_multiple_passo1
                        s1210detPgtoAnt.objects.using(db_slug).filter(id=s1210_detpgtoant_id).update(**dados)
                        obj = s1210detPgtoAnt.objects.using(db_slug).get(id=s1210_detpgtoant_id)
                        #s1210_detpgtoant_editar_custom
                        #s1210_detpgtoant_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(s1210_detpgtoant), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         's1210_detpgtoant', s1210_detpgtoant_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #s1210_detpgtoant_cadastrar_campos_multiple_passo1
                    obj = s1210detPgtoAnt(**dados)
                    obj.save(using = db_slug)
                    #s1210_detpgtoant_cadastrar_custom
                    #s1210_detpgtoant_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's1210_detpgtoant', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('s1210_detpgtoant_apagar', 's1210_detpgtoant_salvar', 's1210_detpgtoant'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if s1210_detpgtoant_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('s1210_detpgtoant_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        s1210_detpgtoant_form = disabled_form_fields(s1210_detpgtoant_form, permissao.permite_editar)
        if s1210_detpgtoant_id:
            if dados_evento['status'] != 0:
                s1210_detpgtoant_form = disabled_form_fields(s1210_detpgtoant_form, 0)
        #s1210_detpgtoant_campos_multiple_passo3

        for field in s1210_detpgtoant_form.fields.keys():
            s1210_detpgtoant_form.fields[field].widget.attrs['ng-model'] = 's1210_detpgtoant_'+field
        if int(dict_hash['print']):
            s1210_detpgtoant_form = disabled_form_for_print(s1210_detpgtoant_form)

        s1210_detpgtoant_infopgtoant_form = None
        s1210_detpgtoant_infopgtoant_lista = None
        if s1210_detpgtoant_id:
            s1210_detpgtoant = get_object_or_404(s1210detPgtoAnt.objects.using( db_slug ), excluido = False, id = s1210_detpgtoant_id)

            s1210_detpgtoant_infopgtoant_form = form_s1210_detpgtoant_infopgtoant(initial={ 's1210_detpgtoant': s1210_detpgtoant }, slug=db_slug)
            s1210_detpgtoant_infopgtoant_form.fields['s1210_detpgtoant'].widget.attrs['readonly'] = True
            s1210_detpgtoant_infopgtoant_lista = s1210detPgtoAntinfoPgtoAnt.objects.using( db_slug ).filter(excluido = False, s1210_detpgtoant_id=s1210_detpgtoant.id).all()
        else:
            s1210_detpgtoant = None
        #s1210_detpgtoant_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1210_detpgtoant' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1210_detpgtoant_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s1210_detpgtoant_id, tabela='s1210_detpgtoant').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's1210_detpgtoant': s1210_detpgtoant,
            's1210_detpgtoant_form': s1210_detpgtoant_form,
            'mensagem': mensagem,
            's1210_detpgtoant_id': int(s1210_detpgtoant_id),
            'usuario': usuario,

            'hash': hash,

            's1210_detpgtoant_infopgtoant_form': s1210_detpgtoant_infopgtoant_form,
            's1210_detpgtoant_infopgtoant_lista': s1210_detpgtoant_infopgtoant_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1210_detpgtoant_salvar_custom_variaveis_context#
        }
        return render(request, 's1210_detpgtoant_salvar.html', context)
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

def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        s1210_detpgtoant_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1210_detpgtoant')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s1210_detpgtoant = get_object_or_404(s1210detPgtoAnt.objects.using( db_slug ), excluido = False, id = s1210_detpgtoant_id)
    dados_evento = {}
    if s1210_detpgtoant_id:
        dados_evento = s1210_detpgtoant.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['s1210_detpgtoant_apagar'] = 0
            dict_permissoes['s1210_detpgtoant_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s1210_detpgtoant), indent=4, sort_keys=True, default=str)
            s1210detPgtoAnt.objects.using( db_slug ).filter(id = s1210_detpgtoant_id).delete()
            #s1210_detpgtoant_apagar_custom
            #s1210_detpgtoant_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's1210_detpgtoant', s1210_detpgtoant_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's1210_detpgtoant_salvar':
            return redirect('s1210_detpgtoant', hash=request.session['retorno_hash'])
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
    return render(request, 's1210_detpgtoant_apagar.html', context)

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

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s1210_detpgtoant_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s1210_detpgtoant')
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
            'show_codcateg': 1,
            'show_s1210_infopgto': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'codcateg': 'codcateg',
                's1210_infopgto': 's1210_infopgto',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'codcateg': 'codcateg',
                's1210_infopgto': 's1210_infopgto',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s1210_detpgtoant_lista = s1210detPgtoAnt.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s1210_detpgtoant_lista) > 100:
            filtrar = True
            s1210_detpgtoant_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s1210_detpgtoant_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's1210_detpgtoant'
        context = {
            's1210_detpgtoant_lista': s1210_detpgtoant_lista,

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
            return render(request, 's1210_detpgtoant_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1210_detpgtoant_listar.html',
                filename="s1210_detpgtoant.pdf",
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
            response = render_to_response('s1210_detpgtoant_listar.html', context)
            filename = "s1210_detpgtoant.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s1210_detpgtoant_csv.html', context)
            filename = "s1210_detpgtoant.csv"
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
