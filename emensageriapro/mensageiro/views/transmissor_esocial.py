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
from emensageriapro.mensageiro.forms import *
from emensageriapro.mensageiro.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
import base64


@login_required
def desvincular_eventos_esocial(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        evento_identidade = dict_hash['id']
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    if evento_identidade:
        a = TransmissorEventosEsocial.objects.using(db_slug).get(identidade=evento_identidade)
        from django.db import connections
        cursor = connections[db_slug].cursor()
        cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=Null WHERE id=%s" % (a.tabela, a.id) )
        messages.success(request, 'Evento desvinculado com sucesso!')
    else:
        messages.error(request, 'Erro ao desvincular evento!')
    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])


@login_required
def vincular_eventos_esocial(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        transmissor_lote_esocial_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    if transmissor_lote_esocial_id:
        transmissor_lote_esocial = get_object_or_404(TransmissorLoteEsocial.objects.using(db_slug), excluido=False,
                                             id=transmissor_lote_esocial_id)
        transmissor_eventos_esocial_vinculados_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(excluido=False,
                                                                                     transmissor_lote_esocial_id=transmissor_lote_esocial_id).all()
        quant = 50 - transmissor_eventos_esocial_vinculados_lista.count()
        transmissor_eventos_esocial_lista = TransmissorEventosEsocial.objects.using(db_slug).filter(excluido=False,
                                                                                     transmissor_lote_esocial__isnull=True,
                                                                                     grupo = transmissor_lote_esocial.grupo
                                                                                     ).all()[:quant]
        from django.db import connections
        n = 0
        for a in transmissor_eventos_esocial_lista:
            cursor = connections[db_slug].cursor()
            cursor.execute("UPDATE %s SET transmissor_lote_esocial_id=%s WHERE id=%s" % (a.tabela, transmissor_lote_esocial_id, a.id) )
            n+=1
        messages.success(request, '%s eventos foram vinculados com sucesso a este transmissor!' % n)
    else:
        messages.error(request, 'Erro ao vincular eventos!')
    return redirect('transmissor_lote_esocial_salvar', hash=dict_hash['return_hash'])