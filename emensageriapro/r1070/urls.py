#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

urlpatterns = patterns('',
    # Examples:



url(r'^r1070-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao.apagar', 
        name='r1070_inclusao_apagar'),

url(r'^r1070-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao.listar', 
        name='r1070_inclusao'),

url(r'^r1070-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao.salvar', 
        name='r1070_inclusao_salvar'),



url(r'^r1070-inclusao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_infosusp.apagar', 
        name='r1070_inclusao_infosusp_apagar'),

url(r'^r1070-inclusao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_infosusp.listar', 
        name='r1070_inclusao_infosusp'),

url(r'^r1070-inclusao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_infosusp.salvar', 
        name='r1070_inclusao_infosusp_salvar'),



url(r'^r1070-inclusao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_dadosprocjud.apagar', 
        name='r1070_inclusao_dadosprocjud_apagar'),

url(r'^r1070-inclusao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_dadosprocjud.listar', 
        name='r1070_inclusao_dadosprocjud'),

url(r'^r1070-inclusao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_inclusao_dadosprocjud.salvar', 
        name='r1070_inclusao_dadosprocjud_salvar'),



url(r'^r1070-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao.apagar', 
        name='r1070_alteracao_apagar'),

url(r'^r1070-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao.listar', 
        name='r1070_alteracao'),

url(r'^r1070-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao.salvar', 
        name='r1070_alteracao_salvar'),



url(r'^r1070-alteracao-infosusp/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_infosusp.apagar', 
        name='r1070_alteracao_infosusp_apagar'),

url(r'^r1070-alteracao-infosusp/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_infosusp.listar', 
        name='r1070_alteracao_infosusp'),

url(r'^r1070-alteracao-infosusp/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_infosusp.salvar', 
        name='r1070_alteracao_infosusp_salvar'),



url(r'^r1070-alteracao-dadosprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_dadosprocjud.apagar', 
        name='r1070_alteracao_dadosprocjud_apagar'),

url(r'^r1070-alteracao-dadosprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_dadosprocjud.listar', 
        name='r1070_alteracao_dadosprocjud'),

url(r'^r1070-alteracao-dadosprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_dadosprocjud.salvar', 
        name='r1070_alteracao_dadosprocjud_salvar'),



url(r'^r1070-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_novavalidade.apagar', 
        name='r1070_alteracao_novavalidade_apagar'),

url(r'^r1070-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_novavalidade.listar', 
        name='r1070_alteracao_novavalidade'),

url(r'^r1070-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_alteracao_novavalidade.salvar', 
        name='r1070_alteracao_novavalidade_salvar'),



url(r'^r1070-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_exclusao.apagar', 
        name='r1070_exclusao_apagar'),

url(r'^r1070-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_exclusao.listar', 
        name='r1070_exclusao'),

url(r'^r1070-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.r1070.views.r1070_exclusao.salvar', 
        name='r1070_exclusao_salvar'),





)