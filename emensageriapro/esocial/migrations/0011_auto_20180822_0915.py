# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0018_auto_20180822_0613'),
        ('esocial', '0010_auto_20180822_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1000evtinfoempregadorocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1005evttabestabocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1005evttabestabocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1005evttabestabocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1010evttabrubricaocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1010evttabrubricaocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1010evttabrubricaocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1020evttablotacaoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1020evttablotacaoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1020evttablotacaoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1030evttabcargoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1030evttabcargoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1030evttabcargoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1035evttabcarreiraocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1035evttabcarreiraocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1035evttabcarreiraocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1040evttabfuncaoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1040evttabfuncaoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1040evttabfuncaoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1050evttabhorturocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1050evttabhorturocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1050evttabhorturocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1060evttabambienteocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1060evttabambienteocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1060evttabambienteocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1070evttabprocessoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1070evttabprocessoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1070evttabprocessoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1080evttaboperportocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1080evttaboperportocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1080evttaboperportocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1200evtremunocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1200evtremunocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1200evtremunocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1202evtrmnrppsocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1202evtrmnrppsocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1202evtrmnrppsocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1207evtbenprrpocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1207evtbenprrpocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1207evtbenprrpocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtosocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtosocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtosocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1250evtaqprodocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1250evtaqprodocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1250evtaqprodocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1260evtcomprodocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1260evtcomprodocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1260evtcomprodocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1270evtcontratavnpocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1270evtcontratavnpocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1270evtcontratavnpocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1280evtinfocomplperocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1280evtinfocomplperocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1280evtinfocomplperocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1295evttotcontingocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1295evttotcontingocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1295evttotcontingocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1298evtreabreevperocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1298evtreabreevperocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1298evtreabreevperocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevperocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevperocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevperocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s1300evtcontrsindpatrocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2190evtadmprelimocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2190evtadmprelimocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2190evtadmprelimocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2200evtadmissaoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2200evtadmissaoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2200evtadmissaoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2205evtaltcadastralocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2205evtaltcadastralocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2205evtaltcadastralocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206evtaltcontratualocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206evtaltcontratualocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2206evtaltcontratualocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2210evtcatocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2210evtcatocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2210evtcatocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2220evtmonitocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2220evtmonitocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2220evtmonitocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2230evtafasttempocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2230evtafasttempocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2230evtafasttempocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2240evtexpriscoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2240evtexpriscoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2240evtexpriscoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2241evtinsapoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2241evtinsapoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2241evtinsapoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2250evtavprevioocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2250evtavprevioocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2250evtavprevioocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2260evtconvintermocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2260evtconvintermocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2260evtconvintermocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2298evtreintegrocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2298evtreintegrocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2298evtreintegrocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2299evtdesligocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2299evtdesligocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2299evtdesligocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2300evttsvinicioocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2300evttsvinicioocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2300evttsvinicioocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2306evttsvaltcontrocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvterminoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvterminoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvterminoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s2400evtcdbenprrpocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s3000evtexclusaoocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s3000evtexclusaoocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s3000evtexclusaoocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5001evtbasestrabocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5001evtbasestrabocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s5001evtbasestrabocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5002evtirrfbenefocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5002evtirrfbenefocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s5002evtirrfbenefocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011evtcsocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011evtcsocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s5011evtcsocorrencias',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5012evtirrfocorrencias',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5012evtirrfocorrencias',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='s5012evtirrfocorrencias',
            name='modificado_por',
        ),
        migrations.AddField(
            model_name='s1000evtinfoempregador',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1000evtinfoempregador_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1005evttabestab',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1005evttabestab_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1010evttabrubrica',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1010evttabrubrica_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1020evttablotacao',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1020evttablotacao_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1030evttabcargo',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1030evttabcargo_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1035evttabcarreira',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1035evttabcarreira_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1040evttabfuncao_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1050evttabhortur_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1060evttabambiente_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1070evttabprocesso_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1080evttaboperport',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1080evttaboperport_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1200evtremun',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1200evtremun_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1202evtrmnrpps',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1202evtrmnrpps_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1207evtbenprrp',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1207evtbenprrp_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1210evtpgtos',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1210evtpgtos_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1250evtaqprod',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1250evtaqprod_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1260evtcomprod',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1260evtcomprod_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1270evtcontratavnp',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1270evtcontratavnp_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1280evtinfocomplper',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1280evtinfocomplper_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1295evttotconting',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1295evttotconting_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1298evtreabreevper',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1298evtreabreevper_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1299evtfechaevper',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1299evtfechaevper_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1300evtcontrsindpatr',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1300evtcontrsindpatr_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2190evtadmprelim',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2190evtadmprelim_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2200evtadmissao',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2200evtadmissao_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2205evtaltcadastral',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2205evtaltcadastral_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2206evtaltcontratual',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2206evtaltcontratual_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2210evtcat',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2210evtcat_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2220evtmonit',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2220evtmonit_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2230evtafasttemp',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2230evtafasttemp_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2240evtexprisco',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2240evtexprisco_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2241evtinsapo',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2241evtinsapo_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2250evtavprevio',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2250evtavprevio_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2260evtconvinterm',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2260evtconvinterm_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2298evtreintegr',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2298evtreintegr_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2299evtdeslig',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2299evtdeslig_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2300evttsvinicio',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2300evttsvinicio_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2306evttsvaltcontr',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2306evttsvaltcontr_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2399evttsvtermino',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2399evttsvtermino_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenprrp',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2400evtcdbenprrp_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s3000evtexclusao',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s3000evtexclusao_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s5001evtbasestrab',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s5001evtbasestrab_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s5002evtirrfbenef',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s5002evtirrfbenef_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s5011evtcs',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s5011evtcs_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s5012evtirrf',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s5012evtirrf_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.DeleteModel(
            name='s1000evtInfoEmpregadorOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1005evtTabEstabOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1010evtTabRubricaOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1020evtTabLotacaoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1030evtTabCargoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1035evtTabCarreiraOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1040evtTabFuncaoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1050evtTabHorTurOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1060evtTabAmbienteOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1070evtTabProcessoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1080evtTabOperPortOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1200evtRemunOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1202evtRmnRPPSOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1207evtBenPrRPOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1210evtPgtosOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1250evtAqProdOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1260evtComProdOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1270evtContratAvNPOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1280evtInfoComplPerOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1295evtTotContingOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1298evtReabreEvPerOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1299evtFechaEvPerOcorrencias',
        ),
        migrations.DeleteModel(
            name='s1300evtContrSindPatrOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2190evtAdmPrelimOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2200evtAdmissaoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2205evtAltCadastralOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2206evtAltContratualOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2210evtCATOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2220evtMonitOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2230evtAfastTempOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2240evtExpRiscoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2241evtInsApoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2250evtAvPrevioOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2260evtConvIntermOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2298evtReintegrOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2299evtDesligOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2300evtTSVInicioOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2306evtTSVAltContrOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2399evtTSVTerminoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s2400evtCdBenPrRPOcorrencias',
        ),
        migrations.DeleteModel(
            name='s3000evtExclusaoOcorrencias',
        ),
        migrations.DeleteModel(
            name='s5001evtBasesTrabOcorrencias',
        ),
        migrations.DeleteModel(
            name='s5002evtIrrfBenefOcorrencias',
        ),
        migrations.DeleteModel(
            name='s5011evtCSOcorrencias',
        ),
        migrations.DeleteModel(
            name='s5012evtIrrfOcorrencias',
        ),
    ]