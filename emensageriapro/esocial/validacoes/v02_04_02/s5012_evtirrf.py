#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s5012_evtirrf(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtIrrf = doc.eSocial.evtIrrf
    
    if 'perApur' in dir(evtIrrf.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEvento.perApur', evtIrrf.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtIrrf.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEmpregador.tpInsc', evtIrrf.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtIrrf.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.ideEmpregador.nrInsc', evtIrrf.ideEmpregador.nrInsc.cdata, 1, '')
    if 'nrRecArqBase' in dir(evtIrrf.infoIRRF): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.infoIRRF.nrRecArqBase', evtIrrf.infoIRRF.nrRecArqBase.cdata, 0, '')
    if 'indExistInfo' in dir(evtIrrf.infoIRRF): validacoes_lista = validar_campo(validacoes_lista,'evtIrrf.infoIRRF.indExistInfo', evtIrrf.infoIRRF.indExistInfo.cdata, 1, '1;2;3')
    if 'infoCRContrib' in dir(evtIrrf.infoIRRF):
        for infoCRContrib in evtIrrf.infoIRRF.infoCRContrib:
            
            if 'tpCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.tpCR', infoCRContrib.tpCR.cdata, 1, '047301;056107;056108;056109;056110;056111;056112;056113;058806;061001;3533;356201')
            if 'vrCR' in dir(infoCRContrib): validacoes_lista = validar_campo(validacoes_lista,'infoCRContrib.vrCR', infoCRContrib.vrCR.cdata, 1, '')

    return validacoes_lista