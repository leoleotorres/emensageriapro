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



url(r'^s1080-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.apagar', 
        name='s1080_inclusao_apagar'),

url(r'^s1080-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.listar', 
        name='s1080_inclusao'),

url(r'^s1080-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_inclusao.salvar', 
        name='s1080_inclusao_salvar'),



url(r'^s1080-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.apagar', 
        name='s1080_alteracao_apagar'),

url(r'^s1080-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.listar', 
        name='s1080_alteracao'),

url(r'^s1080-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao.salvar', 
        name='s1080_alteracao_salvar'),



url(r'^s1080-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.apagar', 
        name='s1080_alteracao_novavalidade_apagar'),

url(r'^s1080-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.listar', 
        name='s1080_alteracao_novavalidade'),

url(r'^s1080-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_alteracao_novavalidade.salvar', 
        name='s1080_alteracao_novavalidade_salvar'),



url(r'^s1080-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.apagar', 
        name='s1080_exclusao_apagar'),

url(r'^s1080-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.listar', 
        name='s1080_exclusao'),

url(r'^s1080-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1080.views.s1080_exclusao.salvar', 
        name='s1080_exclusao_salvar'),





)