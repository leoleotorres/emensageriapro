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
        importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)
    if request.method == 'POST':
        ImportacaoArquivos.objects.using( db_slug ).filter(id = importacao_arquivos_id).update(excluido = True)
        #importacao_arquivos_apagar_custom
        #importacao_arquivos_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'importacao_arquivos_salvar':
            return redirect('importacao_arquivos', hash=request.session['retorno_hash'])
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
    return render(request, 'importacao_arquivos_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        importacao_arquivos_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if importacao_arquivos_id:
        importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if importacao_arquivos_id:
            importacao_arquivos_form = form_importacao_arquivos(request.POST or None, instance = importacao_arquivos, slug = db_slug)
        else:
            importacao_arquivos_form = form_importacao_arquivos(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if importacao_arquivos_form.is_valid():
                dados = importacao_arquivos_form.cleaned_data
                if importacao_arquivos_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #importacao_arquivos_campos_multiple_passo1
                    ImportacaoArquivos.objects.using(db_slug).filter(id=importacao_arquivos_id).update(**dados)
                    obj = ImportacaoArquivos.objects.using(db_slug).get(id=importacao_arquivos_id)
                    #importacao_arquivos_editar_custom
                    #importacao_arquivos_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #importacao_arquivos_cadastrar_campos_multiple_passo1
                    obj = ImportacaoArquivos(**dados)
                    obj.save(using = db_slug)
                    #importacao_arquivos_cadastrar_custom
                    #importacao_arquivos_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('importacao_arquivos_apagar', 'importacao_arquivos_salvar', 'importacao_arquivos'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if importacao_arquivos_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('importacao_arquivos_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        importacao_arquivos_form = disabled_form_fields(importacao_arquivos_form, permissao.permite_editar)
        #importacao_arquivos_campos_multiple_passo3

        for field in importacao_arquivos_form.fields.keys():
            importacao_arquivos_form.fields[field].widget.attrs['ng-model'] = 'importacao_arquivos_'+field
        if int(dict_hash['print']):
            importacao_arquivos_form = disabled_form_for_print(importacao_arquivos_form)

        importacao_arquivos_eventos_form = None
        importacao_arquivos_eventos_lista = None
        if importacao_arquivos_id:
            importacao_arquivos = get_object_or_404(ImportacaoArquivos.objects.using( db_slug ), excluido = False, id = importacao_arquivos_id)

            importacao_arquivos_eventos_form = form_importacao_arquivos_eventos(initial={ 'importacao_arquivos': importacao_arquivos }, slug=db_slug)
            importacao_arquivos_eventos_form.fields['importacao_arquivos'].widget.attrs['readonly'] = True
            importacao_arquivos_eventos_lista = ImportacaoArquivosEventos.objects.using( db_slug ).filter(excluido = False, importacao_arquivos_id=importacao_arquivos.id).all()
        else:
            importacao_arquivos = None
        #importacao_arquivos_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'importacao_arquivos' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'importacao_arquivos_salvar'
        context = {
            'importacao_arquivos': importacao_arquivos,
            'importacao_arquivos_form': importacao_arquivos_form,
            'mensagem': mensagem,
            'importacao_arquivos_id': int(importacao_arquivos_id),
            'usuario': usuario,

            'hash': hash,

            'importacao_arquivos_eventos_form': importacao_arquivos_eventos_form,
            'importacao_arquivos_eventos_lista': importacao_arquivos_eventos_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #importacao_arquivos_salvar_custom_variaveis_context#
        }
        return render(request, 'importacao_arquivos_salvar.html', context)
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
        #importacao_arquivos_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='importacao_arquivos')
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
            'show_quant_error': 0,
            'show_quant_processado': 0,
            'show_quant_aquardando': 0,
            'show_importado_por': 1,
            'show_data_hora': 1,
            'show_status': 1,
            'show_arquivo': 0, }
        post = False
        if request.method == 'POST' and request.FILES['arquivo']:
            from emensageriapro.settings import BASE_DIR
            import os
            from django.core.files.storage import FileSystemStorage
            from emensageriapro.funcoes_importacao import validar_arquivo, importar_arquivo
            myfile = request.FILES['arquivo']
            fs = FileSystemStorage(location=BASE_DIR+'/arquivos/Importacao/enviado/')
            nome_arquivo = myfile.name.replace(' ', '-')
            filename = fs.save(nome_arquivo, myfile)
            arquivo_destino = BASE_DIR + '/arquivos/Importacao/erro/' + filename
            dados_importacao = {}
            dados_importacao['arquivo'] = arquivo_destino
            dados_importacao['status'] = 0
            dados_importacao['data_hora'] = datetime.datetime.now()
            dados_importacao['quant_processado'] = 0
            dados_importacao['quant_error'] = 0
            dados_importacao['quant_aquardando'] = 0
            dados_importacao['importado_por_id'] = usuario_id
            dados_importacao['criado_em'] = datetime.datetime.now()
            dados_importacao['criado_por_id'] = usuario_id
            dados_importacao['excluido'] = False
            obj = ImportacaoArquivos(**dados_importacao)
            obj.save(using=db_slug)
            messages.success(request, 'Arquivo salvo com sucesso! Aguardando processamento...')

            post = True
            dict_fields = {
                'quant_error': 'quant_error',
                'quant_processado': 'quant_processado',
                'quant_aquardando': 'quant_aquardando',
                'importado_por': 'importado_por',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'arquivo__icontains': 'arquivo__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'quant_error': 'quant_error',
                'quant_processado': 'quant_processado',
                'quant_aquardando': 'quant_aquardando',
                'importado_por': 'importado_por',
                'data_hora__range': 'data_hora__range',
                'status': 'status',
                'arquivo__icontains': 'arquivo__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        importacao_arquivos_lista = ImportacaoArquivos.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(importacao_arquivos_lista) > 100:
            filtrar = True
            importacao_arquivos_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        importado_por_lista = Usuarios.objects.using( db_slug ).filter(excluido = False).all()
        #importacao_arquivos_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'importacao_arquivos'
        context = {
            'importacao_arquivos_lista': importacao_arquivos_lista,

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

            'importado_por_lista': importado_por_lista,
        }
        return render(request, 'importacao_arquivos_listar.html', context)
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
