# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s5011basesAquis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indaquis', models.IntegerField(choices=[(1, '1 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral'), (2, '2 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA'), (3, '3 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA. Evento de origem (S- 1250)'), (4, '4 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (5, '5 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (6, '6 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)')])),
                ('vlraquis', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenarnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpcalcpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratcalcpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenardesc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenarcalc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011basesaquis_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011basesaquis_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_ideestab', 'indaquis', 'vlraquis', 'vrcpdescpr', 'vrcpnret', 'vrratnret', 'vrsenarnret', 'vrcpcalcpr', 'vrratdescpr', 'vrratcalcpr', 'vrsenardesc', 'vrsenarcalc'],
                'db_table': 's5011_basesaquis',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011basesAvNPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vrbccp00', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp15', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp20', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp25', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp13', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbcfgts', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdesccp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011basesavnport_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011basesavnport_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp'],
                'db_table': 's5011_basesavnport',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011basesComerc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indcomerc', models.IntegerField(choices=[(2, '2 - Comercializa\xe7\xe3o da Produ\xe7\xe3o efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa f\xedsica por Produtor Rural Pessoa F\xedsica, inclusive por Segurado Especial ou por Pessoa F\xedsica n\xe3o produtor rural'), (3, '3 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PF/Seg. Especia - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA) ou a Intermedi\xe1rio PF'), (7, '7 - Comercializa\xe7\xe3o da Produ\xe7\xe3o Isenta de acordo com a Lei no 13.606/2018'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o da Pessoa F\xedsica/Segurado Especial para Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o da Produ\xe7\xe3o no Mercado Externo')])),
                ('vrbccompr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrratsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrsenarsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011basescomerc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011basescomerc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_ideestab', 'indcomerc', 'vrbccompr', 'vrcpsusp', 'vrratsusp', 'vrsenarsusp'],
                'db_table': 's5011_basescomerc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011basesRemun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indincid', models.IntegerField(choices=[(1, '1 - Normal'), (2, '2 - Ativ. Concomitante'), (9, '9 - Substitu\xedda ou Isenta')])),
                ('codcateg', models.IntegerField()),
                ('vrbccp00', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp15', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp20', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp25', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsuspbccp00', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsuspbccp15', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsuspbccp20', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsuspbccp25', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdescsest', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcalcsest', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdescsenat', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcalcsenat', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsalfam', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsalmat', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011basesremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011basesremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'indincid', 'codcateg', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrsuspbccp00', 'vrsuspbccp15', 'vrsuspbccp20', 'vrsuspbccp25', 'vrdescsest', 'vrcalcsest', 'vrdescsenat', 'vrcalcsenat', 'vrsalfam', 'vrsalmat'],
                'db_table': 's5011_basesremun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011dadosOpPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjopportuario', models.CharField(max_length=14)),
                ('aliqrat', models.IntegerField(choices=[(1, '1 - 1'), (1, '1 - 1'), (2, '2 - 2'), (2, '2 - 2'), (3, '3 - 3'), (3, '3 - 3')])),
                ('fap', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('aliqratajust', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011dadosopport_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011dadosopport_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'cnpjopportuario', 'aliqrat', 'fap', 'aliqratajust'],
                'db_table': 's5011_dadosopport',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011ideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011ideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011ideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_evtcs', models.ForeignKey(related_name='s5011ideestab_s5011_evtcs', to='esocial.s5011evtCS')),
            ],
            options={
                'ordering': ['s5011_evtcs', 'tpinsc', 'nrinsc'],
                'db_table': 's5011_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011ideLotacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codlotacao', models.CharField(max_length=30)),
                ('fpas', models.IntegerField()),
                ('codtercs', models.CharField(max_length=4)),
                ('codtercssusp', models.CharField(max_length=4, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011idelotacao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011idelotacao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_ideestab', models.ForeignKey(related_name='s5011idelotacao_s5011_ideestab', to='s5011.s5011ideEstab')),
            ],
            options={
                'ordering': ['s5011_ideestab', 'codlotacao', 'fpas', 'codtercs', 'codtercssusp'],
                'db_table': 's5011_idelotacao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoAtConc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fatormes', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('fator13', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infoatconc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infoatconc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_infopj', 'fatormes', 'fator13'],
                'db_table': 's5011_infoatconc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoComplObra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indsubstpatrobra', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Patronal Substitu\xedda'), (2, '2 - Contribui\xe7\xe3o Patronal N\xe3o Substitu\xedda')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infocomplobra_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infocomplobra_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5011_infoestab', 'indsubstpatrobra'],
                'db_table': 's5011_infocomplobra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoCPSeg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vrdesccp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpseg', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infocpseg_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infocpseg_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_evtcs', models.OneToOneField(related_name='s5011infocpseg_s5011_evtcs', to='esocial.s5011evtCS')),
            ],
            options={
                'ordering': ['s5011_evtcs', 'vrdesccp', 'vrcpseg'],
                'db_table': 's5011_infocpseg',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoCRContrib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpcr', models.IntegerField()),
                ('vrcr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcrsusp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infocrcontrib_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infocrcontrib_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_evtcs', models.ForeignKey(related_name='s5011infocrcontrib_s5011_evtcs', to='esocial.s5011evtCS')),
            ],
            options={
                'ordering': ['s5011_evtcs', 'tpcr', 'vrcr', 'vrcrsusp'],
                'db_table': 's5011_infocrcontrib',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoCREstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpcr', models.IntegerField()),
                ('vrcr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsuspcr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infocrestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infocrestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_ideestab', models.ForeignKey(related_name='s5011infocrestab_s5011_ideestab', to='s5011.s5011ideEstab')),
            ],
            options={
                'ordering': ['s5011_ideestab', 'tpcr', 'vrcr', 'vrsuspcr'],
                'db_table': 's5011_infocrestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoEmprParcial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsccontrat', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsccontrat', models.CharField(max_length=14)),
                ('tpinscprop', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinscprop', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infoemprparcial_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infoemprparcial_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_idelotacao', models.OneToOneField(related_name='s5011infoemprparcial_s5011_idelotacao', to='s5011.s5011ideLotacao')),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop'],
                'db_table': 's5011_infoemprparcial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnaeprep', models.IntegerField()),
                ('aliqrat', models.IntegerField(choices=[(1, '1 - 1'), (1, '1 - 1'), (2, '2 - 2'), (2, '2 - 2'), (3, '3 - 3'), (3, '3 - 3')])),
                ('fap', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('aliqratajust', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infoestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infoestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_ideestab', models.OneToOneField(related_name='s5011infoestab_s5011_ideestab', to='s5011.s5011ideEstab')),
            ],
            options={
                'ordering': ['s5011_ideestab', 'cnaeprep', 'aliqrat', 'fap', 'aliqratajust'],
                'db_table': 's5011_infoestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoPJ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indcoop', models.IntegerField(blank=True, null=True, choices=[(0, '0 - N\xe3o \xe9 cooperativa'), (1, '1 - Cooperativa de Trabalho'), (2, '2 - Cooperativa de Produ\xe7\xe3o'), (3, '3 - Outras Cooperativas')])),
                ('indconstr', models.IntegerField(choices=[(0, '0 - N\xe3o \xe9 Construtora'), (1, '1 - Empresa Construtora')])),
                ('indsubstpatr', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Integralmente substitu\xedda'), (2, '2 - Parcialmente substitu\xedda')])),
                ('percredcontrib', models.DecimalField(max_length=5, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infopj_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infopj_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_evtcs', models.OneToOneField(related_name='s5011infopj_s5011_evtcs', to='esocial.s5011evtCS')),
            ],
            options={
                'ordering': ['s5011_evtcs', 'indcoop', 'indconstr', 'indsubstpatr', 'percredcontrib'],
                'db_table': 's5011_infopj',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoSubstPatrOpPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjopportuario', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infosubstpatropport_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infosubstpatropport_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_idelotacao', models.ForeignKey(related_name='s5011infosubstpatropport_s5011_idelotacao', to='s5011.s5011ideLotacao')),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'cnpjopportuario'],
                'db_table': 's5011_infosubstpatropport',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5011infoTercSusp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codterc', models.CharField(max_length=4)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5011infotercsusp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5011infotercsusp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5011_idelotacao', models.ForeignKey(related_name='s5011infotercsusp_s5011_idelotacao', to='s5011.s5011ideLotacao')),
            ],
            options={
                'ordering': ['s5011_idelotacao', 'codterc'],
                'db_table': 's5011_infotercsusp',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s5011infocomplobra',
            name='s5011_infoestab',
            field=models.OneToOneField(related_name='s5011infocomplobra_s5011_infoestab', to='s5011.s5011infoEstab'),
        ),
        migrations.AddField(
            model_name='s5011infoatconc',
            name='s5011_infopj',
            field=models.OneToOneField(related_name='s5011infoatconc_s5011_infopj', to='s5011.s5011infoPJ'),
        ),
        migrations.AddField(
            model_name='s5011dadosopport',
            name='s5011_idelotacao',
            field=models.OneToOneField(related_name='s5011dadosopport_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='s5011_idelotacao',
            field=models.ForeignKey(related_name='s5011basesremun_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AddField(
            model_name='s5011basescomerc',
            name='s5011_ideestab',
            field=models.ForeignKey(related_name='s5011basescomerc_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
        migrations.AddField(
            model_name='s5011basesavnport',
            name='s5011_idelotacao',
            field=models.OneToOneField(related_name='s5011basesavnport_s5011_idelotacao', to='s5011.s5011ideLotacao'),
        ),
        migrations.AddField(
            model_name='s5011basesaquis',
            name='s5011_ideestab',
            field=models.ForeignKey(related_name='s5011basesaquis_s5011_ideestab', to='s5011.s5011ideEstab'),
        ),
    ]
