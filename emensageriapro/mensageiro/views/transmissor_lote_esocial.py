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
from emensageriapro.esocial.models import s1000evtInfoEmpregador
from emensageriapro.esocial.models import s1005evtTabEstab
from emensageriapro.esocial.models import s1010evtTabRubrica
from emensageriapro.esocial.models import s1020evtTabLotacao
from emensageriapro.esocial.models import s1030evtTabCargo
from emensageriapro.esocial.models import s1035evtTabCarreira
from emensageriapro.esocial.models import s1040evtTabFuncao
from emensageriapro.esocial.models import s1050evtTabHorTur
from emensageriapro.esocial.models import s1060evtTabAmbiente
from emensageriapro.esocial.models import s1070evtTabProcesso
from emensageriapro.esocial.models import s1080evtTabOperPort
from emensageriapro.esocial.models import s1200evtRemun
from emensageriapro.esocial.models import s1202evtRmnRPPS
from emensageriapro.esocial.models import s1207evtBenPrRP
from emensageriapro.esocial.models import s1210evtPgtos
from emensageriapro.esocial.models import s1250evtAqProd
from emensageriapro.esocial.models import s1260evtComProd
from emensageriapro.esocial.models import s1270evtContratAvNP
from emensageriapro.esocial.models import s1280evtInfoComplPer
from emensageriapro.esocial.models import s1295evtTotConting
from emensageriapro.esocial.models import s1298evtReabreEvPer
from emensageriapro.esocial.models import s1299evtFechaEvPer
from emensageriapro.esocial.models import s1300evtContrSindPatr
from emensageriapro.esocial.models import s2190evtAdmPrelim
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.models import s2241evtInsApo
from emensageriapro.esocial.models import s2250evtAvPrevio
from emensageriapro.esocial.models import s2260evtConvInterm
from emensageriapro.esocial.models import s2298evtReintegr
from emensageriapro.esocial.models import s2299evtDeslig
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.models import s2400evtCdBenPrRP
from emensageriapro.esocial.models import s3000evtExclusao
from emensageriapro.esocial.models import s5001evtBasesTrab
from emensageriapro.esocial.models import s5002evtIrrfBenef
from emensageriapro.esocial.models import s5011evtCS
from emensageriapro.esocial.models import s5012evtIrrf
from emensageriapro.esocial.forms import form_s1000_evtinfoempregador
from emensageriapro.esocial.forms import form_s1005_evttabestab
from emensageriapro.esocial.forms import form_s1010_evttabrubrica
from emensageriapro.esocial.forms import form_s1020_evttablotacao
from emensageriapro.esocial.forms import form_s1030_evttabcargo
from emensageriapro.esocial.forms import form_s1035_evttabcarreira
from emensageriapro.esocial.forms import form_s1040_evttabfuncao
from emensageriapro.esocial.forms import form_s1050_evttabhortur
from emensageriapro.esocial.forms import form_s1060_evttabambiente
from emensageriapro.esocial.forms import form_s1070_evttabprocesso
from emensageriapro.esocial.forms import form_s1080_evttaboperport
from emensageriapro.esocial.forms import form_s1200_evtremun
from emensageriapro.esocial.forms import form_s1202_evtrmnrpps
from emensageriapro.esocial.forms import form_s1207_evtbenprrp
from emensageriapro.esocial.forms import form_s1210_evtpgtos
from emensageriapro.esocial.forms import form_s1250_evtaqprod
from emensageriapro.esocial.forms import form_s1260_evtcomprod
from emensageriapro.esocial.forms import form_s1270_evtcontratavnp
from emensageriapro.esocial.forms import form_s1280_evtinfocomplper
from emensageriapro.esocial.forms import form_s1295_evttotconting
from emensageriapro.esocial.forms import form_s1298_evtreabreevper
from emensageriapro.esocial.forms import form_s1299_evtfechaevper
from emensageriapro.esocial.forms import form_s1300_evtcontrsindpatr
from emensageriapro.esocial.forms import form_s2190_evtadmprelim
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.forms import form_s2241_evtinsapo
from emensageriapro.esocial.forms import form_s2250_evtavprevio
from emensageriapro.esocial.forms import form_s2260_evtconvinterm
from emensageriapro.esocial.forms import form_s2298_evtreintegr
from emensageriapro.esocial.forms import form_s2299_evtdeslig
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.esocial.forms import form_s2400_evtcdbenprrp
from emensageriapro.esocial.forms import form_s3000_evtexclusao
from emensageriapro.esocial.forms import form_s5001_evtbasestrab
from emensageriapro.esocial.forms import form_s5002_evtirrfbenef
from emensageriapro.esocial.forms import form_s5011_evtcs
from emensageriapro.esocial.forms import form_s5012_evtirrf

#IMPORTACOES


def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)
    if request.method == 'POST':
        TransmissorLoteEsocial.objects.using( db_slug ).filter(id = transmissor_lote_esocial_id).update(excluido = True)
        #transmissor_lote_esocial_apagar_custom
        #transmissor_lote_esocial_apagar_custom
        messages.success(request, 'Apagado com sucesso!')
        if request.session['retorno_pagina']== 'transmissor_lote_esocial_salvar':
            return redirect('transmissor_lote_esocial', hash=request.session['retorno_hash'])
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
    return render(request, 'transmissor_lote_esocial_apagar.html', context)

def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if transmissor_lote_esocial_id:
        transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if transmissor_lote_esocial_id:
            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None, instance = transmissor_lote_esocial, slug = db_slug)
        else:
            transmissor_lote_esocial_form = form_transmissor_lote_esocial(request.POST or None, slug = db_slug, initial={'status': 0})
        if request.method == 'POST':
            if transmissor_lote_esocial_form.is_valid():
                dados = transmissor_lote_esocial_form.cleaned_data
                if transmissor_lote_esocial_id:
                    dados['modificado_por_id'] = usuario_id
                    dados['modificado_em'] = datetime.datetime.now()
                    #transmissor_lote_esocial_campos_multiple_passo1
                    TransmissorLoteEsocial.objects.using(db_slug).filter(id=transmissor_lote_esocial_id).update(**dados)
                    obj = TransmissorLoteEsocial.objects.using(db_slug).get(id=transmissor_lote_esocial_id)
                    #transmissor_lote_esocial_editar_custom
                    #transmissor_lote_esocial_campos_multiple_passo2
                    messages.success(request, 'Alterado com sucesso!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #transmissor_lote_esocial_cadastrar_campos_multiple_passo1
                    obj = TransmissorLoteEsocial(**dados)
                    obj.save(using = db_slug)
                    #transmissor_lote_esocial_cadastrar_custom
                    #transmissor_lote_esocial_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                if request.session['retorno_pagina'] not in ('transmissor_lote_esocial_apagar', 'transmissor_lote_esocial_salvar', 'transmissor_lote_esocial'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if transmissor_lote_esocial_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('transmissor_lote_esocial_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        transmissor_lote_esocial_form = disabled_form_fields(transmissor_lote_esocial_form, permissao.permite_editar)
        #transmissor_lote_esocial_campos_multiple_passo3

        for field in transmissor_lote_esocial_form.fields.keys():
            transmissor_lote_esocial_form.fields[field].widget.attrs['ng-model'] = 'transmissor_lote_esocial_'+field
        if int(dict_hash['print']):
            transmissor_lote_esocial_form = disabled_form_for_print(transmissor_lote_esocial_form)

        transmissor_lote_esocial_ocorrencias_form = None
        transmissor_lote_esocial_ocorrencias_lista = None
        if transmissor_lote_esocial_id:
            transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using( db_slug ), excluido = False, id = transmissor_lote_esocial_id)

            transmissor_lote_esocial_ocorrencias_form = form_transmissor_lote_esocial_ocorrencias(initial={ 'transmissor_lote_esocial': transmissor_lote_esocial }, slug=db_slug)
            transmissor_lote_esocial_ocorrencias_form.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
            transmissor_lote_esocial_ocorrencias_lista = TransmissorLoteEsocialOcorrencias.objects.using( db_slug ).filter(excluido = False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
        else:
            transmissor_lote_esocial = None
        if transmissor_lote_esocial:
            transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(excluido=False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
            transmissor_eventos_esocial_totalizacoes_lista = TransmissorEventosEsocialTotalizacoes.objects.using(db_slug).filter(excluido=False, transmissor_lote_esocial_id=transmissor_lote_esocial.id).all()
        else:
            transmissor_eventos_esocial_lista = None
            transmissor_eventos_esocial_totalizacoes_lista = None
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]

        if dict_hash['tab'] or 'transmissor_lote_esocial' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'transmissor_lote_esocial_salvar'
        context = {
            'transmissor_lote_esocial': transmissor_lote_esocial,
            'transmissor_lote_esocial_form': transmissor_lote_esocial_form,
            'mensagem': mensagem,
            'transmissor_lote_esocial_id': int(transmissor_lote_esocial_id),
            'usuario': usuario,

            'hash': hash,

            'transmissor_lote_esocial_ocorrencias_form': transmissor_lote_esocial_ocorrencias_form,
            'transmissor_lote_esocial_ocorrencias_lista': transmissor_lote_esocial_ocorrencias_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            'transmissor_eventos_esocial_lista': transmissor_eventos_esocial_lista,
'transmissor_eventos_esocial_totalizacoes_lista': transmissor_eventos_esocial_totalizacoes_lista,
        }
        return render(request, 'transmissor_lote_esocial_salvar.html', context)

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
        #transmissor_lote_esocial_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='transmissor_lote_esocial')
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
            'show_tempo_estimado_conclusao': 0,
            'show_processamento_versao_aplicativo': 0,
            'show_protocolo': 0,
            'show_recepcao_versao_aplicativo': 0,
            'show_recepcao_data_hora': 0,
            'show_resposta_descricao': 0,
            'show_resposta_codigo': 1,
            'show_status': 1,
            'show_grupo': 1,
            'show_empregador_nrinsc': 1,
            'show_empregador_tpinsc': 1,
            'show_transmissor': 0, }
        post = False
        #ANTES-POST-LISTAGEM
        if request.method == 'POST':
            post = True
            dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'resposta_codigo': 'resposta_codigo',
                'status': 'status',
                'grupo': 'grupo',
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',
                'transmissor': 'transmissor',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'tempo_estimado_conclusao': 'tempo_estimado_conclusao',
                'processamento_versao_aplicativo__icontains': 'processamento_versao_aplicativo__icontains',
                'protocolo__icontains': 'protocolo__icontains',
                'recepcao_versao_aplicativo__icontains': 'recepcao_versao_aplicativo__icontains',
                'recepcao_data_hora__range': 'recepcao_data_hora__range',
                'resposta_codigo': 'resposta_codigo',
                'status': 'status',
                'grupo': 'grupo',
                'empregador_nrinsc__icontains': 'empregador_nrinsc__icontains',
                'empregador_tpinsc': 'empregador_tpinsc',
                'transmissor': 'transmissor',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        transmissor_lote_esocial_lista = TransmissorLoteEsocial.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(transmissor_lote_esocial_lista) > 100:
            filtrar = True
            transmissor_lote_esocial_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lista = TransmissorLote.objects.using( db_slug ).filter(excluido = False).all()
        #transmissor_lote_esocial_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'transmissor_lote_esocial'
        context = {
            'transmissor_lote_esocial_lista': transmissor_lote_esocial_lista,

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

            'transmissor_lista': transmissor_lista,
        }
        return render(request, 'transmissor_lote_esocial_listar.html', context)
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
