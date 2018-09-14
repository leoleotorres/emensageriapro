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



url(r'^s1250-tpaquis/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.apagar', 
        name='s1250_tpaquis_apagar'),

url(r'^s1250-tpaquis/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.listar', 
        name='s1250_tpaquis'),

url(r'^s1250-tpaquis/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_tpaquis.salvar', 
        name='s1250_tpaquis_salvar'),



url(r'^s1250-ideprodutor/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.apagar', 
        name='s1250_ideprodutor_apagar'),

url(r'^s1250-ideprodutor/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.listar', 
        name='s1250_ideprodutor'),

url(r'^s1250-ideprodutor/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_ideprodutor.salvar', 
        name='s1250_ideprodutor_salvar'),



url(r'^s1250-nfs/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.apagar', 
        name='s1250_nfs_apagar'),

url(r'^s1250-nfs/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.listar', 
        name='s1250_nfs'),

url(r'^s1250-nfs/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_nfs.salvar', 
        name='s1250_nfs_salvar'),



url(r'^s1250-infoprocjud/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.apagar', 
        name='s1250_infoprocjud_apagar'),

url(r'^s1250-infoprocjud/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.listar', 
        name='s1250_infoprocjud'),

url(r'^s1250-infoprocjud/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1250.views.s1250_infoprocjud.salvar', 
        name='s1250_infoprocjud_salvar'),





)