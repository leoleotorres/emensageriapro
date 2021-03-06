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



ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

CHOICES_S2220_INDRESULT = (
    (1, u'1 - Normal'),
    (2, u'2 - Alterado'),
    (3, u'3 - Estável'),
    (4, u'4 - Agravamento'),
)

CHOICES_S2220_INTERPREXM = (
    (1, u'1 - EE'),
    (2, u'2 - SC'),
    (3, u'3 - SC+'),
)

CHOICES_S2220_ORDEXAME = (
    (1, u'1 - Referencial'),
    (2, u'2 - Sequencial'),
)

CHOICES_S2220_TPEXAMEOCUP = (
    (0, u'0 - Exame médico ocupacional'),
    (1, u'1 - Exame toxicológico do motorista profissional'),
)

class s2220exMedOcup(models.Model):
    s2220_evtmonit = models.OneToOneField('esocial.s2220evtMonit',
        related_name='%(class)s_s2220_evtmonit')
    tpexameocup = models.IntegerField(choices=CHOICES_S2220_TPEXAMEOCUP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2220_evtmonit) + ' - ' + unicode(self.tpexameocup)
    #s2220_exmedocup_custom#
    #s2220_exmedocup_custom#
    class Meta:
        db_table = r's2220_exmedocup'
        managed = True
        ordering = ['s2220_evtmonit', 'tpexameocup']



class s2220exMedOcupSerializer(ModelSerializer):
    class Meta:
        model = s2220exMedOcup
        fields = '__all__'
            

class s2220exame(models.Model):
    s2220_evtmonit = models.ForeignKey('esocial.s2220evtMonit',
        related_name='%(class)s_s2220_evtmonit')
    dtexm = models.DateField()
    procrealizado = models.IntegerField(blank=True, null=True)
    obsproc = models.CharField(max_length=200, blank=True, null=True)
    interprexm = models.IntegerField(choices=CHOICES_S2220_INTERPREXM)
    ordexame = models.IntegerField(choices=CHOICES_S2220_ORDEXAME)
    dtinimonit = models.DateField()
    dtfimmonit = models.DateField(blank=True, null=True)
    indresult = models.IntegerField(choices=CHOICES_S2220_INDRESULT, blank=True, null=True)
    nisresp = models.CharField(max_length=11)
    nrconsclasse = models.CharField(max_length=8)
    ufconsclasse = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    cpfresp = models.CharField(max_length=11)
    nmresp = models.CharField(max_length=70)
    nrcrm = models.CharField(max_length=8)
    ufcrm = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2220_evtmonit) + ' - ' + unicode(self.dtexm) + ' - ' + unicode(self.procrealizado) + ' - ' + unicode(self.obsproc) + ' - ' + unicode(self.interprexm) + ' - ' + unicode(self.ordexame) + ' - ' + unicode(self.dtinimonit) + ' - ' + unicode(self.dtfimmonit) + ' - ' + unicode(self.indresult) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nrconsclasse) + ' - ' + unicode(self.ufconsclasse) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.nrcrm) + ' - ' + unicode(self.ufcrm)
    #s2220_exame_custom#
    #s2220_exame_custom#
    class Meta:
        db_table = r's2220_exame'
        managed = True
        ordering = ['s2220_evtmonit', 'dtexm', 'procrealizado', 'obsproc', 'interprexm', 'ordexame', 'dtinimonit', 'dtfimmonit', 'indresult', 'nisresp', 'nrconsclasse', 'ufconsclasse', 'cpfresp', 'nmresp', 'nrcrm', 'ufcrm']



class s2220exameSerializer(ModelSerializer):
    class Meta:
        model = s2220exame
        fields = '__all__'
            

class s2220toxicologico(models.Model):
    s2220_evtmonit = models.OneToOneField('esocial.s2220evtMonit',
        related_name='%(class)s_s2220_evtmonit')
    dtexame = models.DateField()
    cnpjlab = models.CharField(max_length=14)
    codseqexame = models.CharField(max_length=11)
    nmmed = models.CharField(max_length=70)
    nrcrm = models.CharField(max_length=8)
    ufcrm = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2220_evtmonit) + ' - ' + unicode(self.dtexame) + ' - ' + unicode(self.cnpjlab) + ' - ' + unicode(self.codseqexame) + ' - ' + unicode(self.nmmed) + ' - ' + unicode(self.nrcrm) + ' - ' + unicode(self.ufcrm)
    #s2220_toxicologico_custom#
    #s2220_toxicologico_custom#
    class Meta:
        db_table = r's2220_toxicologico'
        managed = True
        ordering = ['s2220_evtmonit', 'dtexame', 'cnpjlab', 'codseqexame', 'nmmed', 'nrcrm', 'ufcrm']



class s2220toxicologicoSerializer(ModelSerializer):
    class Meta:
        model = s2220toxicologico
        fields = '__all__'
            

#VIEWS_MODELS
