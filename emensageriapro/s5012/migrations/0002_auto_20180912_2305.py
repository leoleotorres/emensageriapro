# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5012', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5012infocrcontrib',
            name='tpcr',
            field=models.IntegerField(choices=[(3533, '3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pens\xe3o Pagos por Previd\xeancia P\xfablica'), (47301, '047301 - IRRF - Residentes Fiscais no Exterior'), (56107, '056107 - IRRF Mensal, 13\xb0 sal\xe1rio e F\xe9rias sobre Trabalho Assalariado no pa\xeds ou ausente no exterior a servi\xe7o do pa\xeds, exceto se contratado por Empregador Dom\xe9stico ou por Segurado Especial sujeito a recolhimento unificado'), (56108, '056108 - IRRF Mensal, 13\xb0 sal\xe1rio e F\xe9rias sobre Trabalho Assalariado no pa\xeds ou ausente no exterior a servi\xe7o do pa\xeds, Empregado Dom\xe9stico ou Trabalhador contratado por Segurado Especial sujeito a recolhimento unificado'), (56109, '056109 - IRRF 13\xb0 sal\xe1rio na rescis\xe3o de contrato de trabalho relativo a empregador sujeito a recolhimento unificado'), (56110, '056110 - IRRF - Empregado dom\xe9stico - 13\xba sal\xe1rio'), (56111, '056111 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'), (56112, '056112 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio'), (56113, '056113 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio rescis\xf3rio'), (58806, '058806 - IRRF sobre Rendimento do trabalho sem v\xednculo empregat\xedcio'), (61001, '061001 - IRRF sobre Rendimentos relativos a presta\xe7\xe3o de servi\xe7os de transporte rodovi\xe1rio internacional de carga, pagos a transportador aut\xf4nomo PF residente no Paraguai'), (356201, '356201 - IRRF sobre Participa\xe7\xe3o dos trabalhadores em Lucros ou Resultados (PLR).')]),
        ),
    ]
