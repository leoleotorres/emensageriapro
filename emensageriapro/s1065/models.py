#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



PERIODOS = (
    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
)

CHOICES_S1065_ALTERACAO_TPEP = (
    (1, u'1 - Equipamento de Proteção Individual (EPI)'),
    (2, u'2 - Equipamento de Proteção Coletiva (EPC)'),
)

CHOICES_S1065_INCLUSAO_TPEP = (
    (1, u'1 - Equipamento de Proteção Individual (EPI)'),
    (2, u'2 - Equipamento de Proteção Coletiva (EPC)'),
)

class s1065alteracao(models.Model):
    s1065_evttabequipamento = models.OneToOneField('esocial.s1065evtTabEquipamento',
        related_name='%(class)s_s1065_evttabequipamento')
    codep = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    tpep = models.IntegerField(choices=CHOICES_S1065_ALTERACAO_TPEP)
    dscep = models.CharField(max_length=999)
    caepi = models.CharField(max_length=20, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1065_evttabequipamento) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.tpep) + ' - ' + unicode(self.dscep) + ' - ' + unicode(self.caepi)
    #s1065_alteracao_custom#
    #s1065_alteracao_custom#
    class Meta:
        db_table = r's1065_alteracao'
        managed = True
        ordering = ['s1065_evttabequipamento', 'codep', 'inivalid', 'fimvalid', 'tpep', 'dscep', 'caepi']



class s1065alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1065alteracao
        fields = '__all__'
            

class s1065alteracaonovaValidade(models.Model):
    s1065_alteracao = models.OneToOneField('s1065alteracao',
        related_name='%(class)s_s1065_alteracao')
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1065_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1065_alteracao_novavalidade_custom#
    #s1065_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1065_alteracao_novavalidade'
        managed = True
        ordering = ['s1065_alteracao', 'inivalid', 'fimvalid']



class s1065alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1065alteracaonovaValidade
        fields = '__all__'
            

class s1065exclusao(models.Model):
    s1065_evttabequipamento = models.OneToOneField('esocial.s1065evtTabEquipamento',
        related_name='%(class)s_s1065_evttabequipamento')
    codep = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1065_evttabequipamento) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1065_exclusao_custom#
    #s1065_exclusao_custom#
    class Meta:
        db_table = r's1065_exclusao'
        managed = True
        ordering = ['s1065_evttabequipamento', 'codep', 'inivalid', 'fimvalid']



class s1065exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1065exclusao
        fields = '__all__'
            

class s1065inclusao(models.Model):
    s1065_evttabequipamento = models.OneToOneField('esocial.s1065evtTabEquipamento',
        related_name='%(class)s_s1065_evttabequipamento')
    codep = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    tpep = models.IntegerField(choices=CHOICES_S1065_INCLUSAO_TPEP)
    dscep = models.CharField(max_length=999)
    caepi = models.CharField(max_length=20, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1065_evttabequipamento) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.tpep) + ' - ' + unicode(self.dscep) + ' - ' + unicode(self.caepi)
    #s1065_inclusao_custom#
    #s1065_inclusao_custom#
    class Meta:
        db_table = r's1065_inclusao'
        managed = True
        ordering = ['s1065_evttabequipamento', 'codep', 'inivalid', 'fimvalid', 'tpep', 'dscep', 'caepi']



class s1065inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1065inclusao
        fields = '__all__'
            

#VIEWS_MODELS
