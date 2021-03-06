#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1050_evttabhortur(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabHorTur = doc.eSocial.evtTabHorTur
    
    if 'tpAmb' in dir(evtTabHorTur.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabHorTur.ideEvento.tpAmb', evtTabHorTur.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabHorTur.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabHorTur.ideEvento.procEmi', evtTabHorTur.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabHorTur.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabHorTur.ideEvento.verProc', evtTabHorTur.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabHorTur.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabHorTur.ideEmpregador.tpInsc', evtTabHorTur.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabHorTur.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabHorTur.ideEmpregador.nrInsc', evtTabHorTur.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabHorTur.infoHorContratual):
        for inclusao in evtTabHorTur.infoHorContratual.inclusao:
            
            if 'codHorContrat' in dir(inclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideHorContratual.codHorContrat', inclusao.ideHorContratual.codHorContrat.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideHorContratual.iniValid', inclusao.ideHorContratual.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideHorContratual.fimValid', inclusao.ideHorContratual.fimValid.cdata, 0, '')
            if 'hrEntr' in dir(inclusao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosHorContratual.hrEntr', inclusao.dadosHorContratual.hrEntr.cdata, 1, '')
            if 'hrSaida' in dir(inclusao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosHorContratual.hrSaida', inclusao.dadosHorContratual.hrSaida.cdata, 1, '')
            if 'durJornada' in dir(inclusao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosHorContratual.durJornada', inclusao.dadosHorContratual.durJornada.cdata, 1, '')
            if 'perHorFlexivel' in dir(inclusao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosHorContratual.perHorFlexivel', inclusao.dadosHorContratual.perHorFlexivel.cdata, 1, 'S;N')

            if 'horarioIntervalo' in dir(inclusao.dadosHorContratual):
                for horarioIntervalo in inclusao.dadosHorContratual.horarioIntervalo:
                    
                    if 'tpInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.tpInterv', horarioIntervalo.tpInterv.cdata, 1, '1;2')
                    if 'durInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.durInterv', horarioIntervalo.durInterv.cdata, 1, '')
                    if 'iniInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.iniInterv', horarioIntervalo.iniInterv.cdata, 0, '')
                    if 'termInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.termInterv', horarioIntervalo.termInterv.cdata, 0, '')
        
    if 'alteracao' in dir(evtTabHorTur.infoHorContratual):
        for alteracao in evtTabHorTur.infoHorContratual.alteracao:
            
            if 'codHorContrat' in dir(alteracao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideHorContratual.codHorContrat', alteracao.ideHorContratual.codHorContrat.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideHorContratual.iniValid', alteracao.ideHorContratual.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideHorContratual.fimValid', alteracao.ideHorContratual.fimValid.cdata, 0, '')
            if 'hrEntr' in dir(alteracao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosHorContratual.hrEntr', alteracao.dadosHorContratual.hrEntr.cdata, 1, '')
            if 'hrSaida' in dir(alteracao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosHorContratual.hrSaida', alteracao.dadosHorContratual.hrSaida.cdata, 1, '')
            if 'durJornada' in dir(alteracao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosHorContratual.durJornada', alteracao.dadosHorContratual.durJornada.cdata, 1, '')
            if 'perHorFlexivel' in dir(alteracao.dadosHorContratual): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosHorContratual.perHorFlexivel', alteracao.dadosHorContratual.perHorFlexivel.cdata, 1, 'S;N')

            if 'horarioIntervalo' in dir(alteracao.dadosHorContratual):
                for horarioIntervalo in alteracao.dadosHorContratual.horarioIntervalo:
                    
                    if 'tpInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.tpInterv', horarioIntervalo.tpInterv.cdata, 1, '1;2')
                    if 'durInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.durInterv', horarioIntervalo.durInterv.cdata, 1, '')
                    if 'iniInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.iniInterv', horarioIntervalo.iniInterv.cdata, 0, '')
                    if 'termInterv' in dir(horarioIntervalo): validacoes_lista = validar_campo(validacoes_lista,'horarioIntervalo.termInterv', horarioIntervalo.termInterv.cdata, 0, '')
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
    if 'exclusao' in dir(evtTabHorTur.infoHorContratual):
        for exclusao in evtTabHorTur.infoHorContratual.exclusao:
            
            if 'codHorContrat' in dir(exclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideHorContratual.codHorContrat', exclusao.ideHorContratual.codHorContrat.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideHorContratual.iniValid', exclusao.ideHorContratual.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideHorContratual): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideHorContratual.fimValid', exclusao.ideHorContratual.fimValid.cdata, 0, '')

    return validacoes_lista