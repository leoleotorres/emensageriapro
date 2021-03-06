#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s1030_evttabcargo(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabCargo = doc.eSocial.evtTabCargo
    
    if 'tpAmb' in dir(evtTabCargo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCargo.ideEvento.tpAmb', evtTabCargo.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTabCargo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCargo.ideEvento.procEmi', evtTabCargo.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTabCargo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTabCargo.ideEvento.verProc', evtTabCargo.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTabCargo.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCargo.ideEmpregador.tpInsc', evtTabCargo.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTabCargo.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTabCargo.ideEmpregador.nrInsc', evtTabCargo.ideEmpregador.nrInsc.cdata, 1, '')
    if 'inclusao' in dir(evtTabCargo.infoCargo):
        for inclusao in evtTabCargo.infoCargo.inclusao:
            
            if 'codCargo' in dir(inclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCargo.codCargo', inclusao.ideCargo.codCargo.cdata, 1, '')
            if 'iniValid' in dir(inclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCargo.iniValid', inclusao.ideCargo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(inclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.ideCargo.fimValid', inclusao.ideCargo.fimValid.cdata, 0, '')
            if 'nmCargo' in dir(inclusao.dadosCargo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCargo.nmCargo', inclusao.dadosCargo.nmCargo.cdata, 1, '')
            if 'codCBO' in dir(inclusao.dadosCargo): validacoes_lista = validar_campo(validacoes_lista,'inclusao.dadosCargo.codCBO', inclusao.dadosCargo.codCBO.cdata, 1, '')

            if 'cargoPublico' in dir(inclusao.dadosCargo):
                for cargoPublico in inclusao.dadosCargo.cargoPublico:
                    
                    if 'acumCargo' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.acumCargo', cargoPublico.acumCargo.cdata, 1, '1;2;3;4')
                    if 'contagemEsp' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.contagemEsp', cargoPublico.contagemEsp.cdata, 1, '1;2;3;4')
                    if 'dedicExcl' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.dedicExcl', cargoPublico.dedicExcl.cdata, 1, 'S;N')
                    if 'nrLei' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.nrLei', cargoPublico.nrLei.cdata, 1, '')
                    if 'dtLei' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.dtLei', cargoPublico.dtLei.cdata, 1, '')
                    if 'sitCargo' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.sitCargo', cargoPublico.sitCargo.cdata, 1, '1;2;3')
        
    if 'alteracao' in dir(evtTabCargo.infoCargo):
        for alteracao in evtTabCargo.infoCargo.alteracao:
            
            if 'codCargo' in dir(alteracao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCargo.codCargo', alteracao.ideCargo.codCargo.cdata, 1, '')
            if 'iniValid' in dir(alteracao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCargo.iniValid', alteracao.ideCargo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(alteracao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.ideCargo.fimValid', alteracao.ideCargo.fimValid.cdata, 0, '')
            if 'nmCargo' in dir(alteracao.dadosCargo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCargo.nmCargo', alteracao.dadosCargo.nmCargo.cdata, 1, '')
            if 'codCBO' in dir(alteracao.dadosCargo): validacoes_lista = validar_campo(validacoes_lista,'alteracao.dadosCargo.codCBO', alteracao.dadosCargo.codCBO.cdata, 1, '')

            if 'cargoPublico' in dir(alteracao.dadosCargo):
                for cargoPublico in alteracao.dadosCargo.cargoPublico:
                    
                    if 'acumCargo' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.acumCargo', cargoPublico.acumCargo.cdata, 1, '1;2;3;4')
                    if 'contagemEsp' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.contagemEsp', cargoPublico.contagemEsp.cdata, 1, '1;2;3;4')
                    if 'dedicExcl' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.dedicExcl', cargoPublico.dedicExcl.cdata, 1, 'S;N')
                    if 'nrLei' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.nrLei', cargoPublico.nrLei.cdata, 1, '')
                    if 'dtLei' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.dtLei', cargoPublico.dtLei.cdata, 1, '')
                    if 'sitCargo' in dir(cargoPublico): validacoes_lista = validar_campo(validacoes_lista,'cargoPublico.sitCargo', cargoPublico.sitCargo.cdata, 1, '1;2;3')
        
            if 'novaValidade' in dir(alteracao):
                for novaValidade in alteracao.novaValidade:
                    
                    if 'iniValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.iniValid', novaValidade.iniValid.cdata, 1, '')
                    if 'fimValid' in dir(novaValidade): validacoes_lista = validar_campo(validacoes_lista,'novaValidade.fimValid', novaValidade.fimValid.cdata, 0, '')
        
    if 'exclusao' in dir(evtTabCargo.infoCargo):
        for exclusao in evtTabCargo.infoCargo.exclusao:
            
            if 'codCargo' in dir(exclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCargo.codCargo', exclusao.ideCargo.codCargo.cdata, 1, '')
            if 'iniValid' in dir(exclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCargo.iniValid', exclusao.ideCargo.iniValid.cdata, 1, '')
            if 'fimValid' in dir(exclusao.ideCargo): validacoes_lista = validar_campo(validacoes_lista,'exclusao.ideCargo.fimValid', exclusao.ideCargo.fimValid.cdata, 0, '')

    return validacoes_lista