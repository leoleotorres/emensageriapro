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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        regras_validacao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_validacao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    regras_validacao = get_object_or_404(RegrasDeValidacao.objects.using( db_slug ), excluido = False, id = regras_validacao_id)
    if request.method == 'POST':
        RegrasDeValidacao.objects.using( db_slug ).filter(id = regras_validacao_id).update(excluido = True)
        #regras_validacao_apagar_custom
        #regras_validacao_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'regras_validacao_salvar':
            return redirect('regras_validacao', hash=request.session['retorno_hash'])
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
    return render(request, 'regras_validacao_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        regras_validacao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_validacao')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if regras_validacao_id:
        regras_validacao = get_object_or_404(RegrasDeValidacao.objects.using( db_slug ), excluido = False, id = regras_validacao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if regras_validacao_id:
            regras_validacao_form = form_regras_validacao(request.POST or None, instance = regras_validacao, slug = db_slug)
        else:
            regras_validacao_form = form_regras_validacao(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if regras_validacao_form.is_valid():
                dados = regras_validacao_form.cleaned_data
                if regras_validacao_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #regras_validacao_campos_multiple_passo1
                    RegrasDeValidacao.objects.using(db_slug).filter(id=regras_validacao_id).update(**dados)
                    obj = RegrasDeValidacao.objects.using(db_slug).get(id=regras_validacao_id)
                    #regras_validacao_editar_custom
                    #regras_validacao_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #regras_validacao_cadastrar_campos_multiple_passo1
                    obj = RegrasDeValidacao(**dados)
                    obj.save(using = db_slug)
                    #regras_validacao_cadastrar_custom
                    #regras_validacao_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('regras_validacao_apagar', 'regras_validacao_salvar', 'regras_validacao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if regras_validacao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('regras_validacao_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        regras_validacao_form = disabled_form_fields(regras_validacao_form, permissao.permite_editar)
        #regras_validacao_campos_multiple_passo3

        for field in regras_validacao_form.fields.keys():
            regras_validacao_form.fields[field].widget.attrs['ng-model'] = 'regras_validacao_'+field
        if int(dict_hash['print']):
            regras_validacao_form = disabled_form_for_print(regras_validacao_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if regras_validacao_id:
            regras_validacao = get_object_or_404(RegrasDeValidacao.objects.using( db_slug ), excluido = False, id = regras_validacao_id)
            pass
        else:
            regras_validacao = None
        #regras_validacao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'regras_validacao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'regras_validacao_salvar'
        context = {
            'regras_validacao': regras_validacao,
            'regras_validacao_form': regras_validacao_form,
            'mensagem': mensagem,
            'regras_validacao_id': int(regras_validacao_id),
            'usuario': usuario,

            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #regras_validacao_salvar_custom_variaveis_context#
        }
        return render(request, 'regras_validacao_salvar.html', context)
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

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #regras_validacao_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='regras_validacao')
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
            'show_validacoes': 0,
            'show_validacoes_precedencia': 0,
            'show_valores_validos': 0,
            'show_tabela': 0,
            'show_descricao': 0,
            'show_obrigatorio': 0,
            'show_casas_decimais': 0,
            'show_tamanho': 0,
            'show_ocorrencias': 0,
            'show_tipo': 0,
            'show_elemento': 0,
            'show_registro_pai': 1,
            'show_registro_campo': 1,
            'show_numero': 1,
            'show_versao': 1,
            'show_evento': 1, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'validacoes_precedencia__icontains': 'validacoes_precedencia__icontains',
                'valores_validos__icontains': 'valores_validos__icontains',
                'tabela__icontains': 'tabela__icontains',
                'descricao__icontains': 'descricao__icontains',
                'obrigatorio': 'obrigatorio',
                'casas_decimais__icontains': 'casas_decimais__icontains',
                'tamanho__icontains': 'tamanho__icontains',
                'ocorrencias__icontains': 'ocorrencias__icontains',
                'tipo__icontains': 'tipo__icontains',
                'elemento__icontains': 'elemento__icontains',
                'registro_pai__icontains': 'registro_pai__icontains',
                'registro_campo__icontains': 'registro_campo__icontains',
                'numero': 'numero',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'validacoes__icontains': 'validacoes__icontains',
                'validacoes_precedencia__icontains': 'validacoes_precedencia__icontains',
                'valores_validos__icontains': 'valores_validos__icontains',
                'tabela__icontains': 'tabela__icontains',
                'descricao__icontains': 'descricao__icontains',
                'obrigatorio': 'obrigatorio',
                'casas_decimais__icontains': 'casas_decimais__icontains',
                'tamanho__icontains': 'tamanho__icontains',
                'ocorrencias__icontains': 'ocorrencias__icontains',
                'tipo__icontains': 'tipo__icontains',
                'elemento__icontains': 'elemento__icontains',
                'registro_pai__icontains': 'registro_pai__icontains',
                'registro_campo__icontains': 'registro_campo__icontains',
                'numero': 'numero',
                'versao__icontains': 'versao__icontains',
                'evento__icontains': 'evento__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        regras_validacao_lista = RegrasDeValidacao.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(regras_validacao_lista) > 100:
            filtrar = True
            regras_validacao_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #regras_validacao_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'regras_validacao'
        context = {
            'regras_validacao_lista': regras_validacao_lista,

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
        return render(request, 'regras_validacao_listar.html', context)
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
