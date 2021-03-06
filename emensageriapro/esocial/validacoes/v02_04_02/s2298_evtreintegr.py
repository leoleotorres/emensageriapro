#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2298_evtreintegr(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtReintegr = doc.eSocial.evtReintegr
    
    if 'indRetif' in dir(evtReintegr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEvento.indRetif', evtReintegr.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtReintegr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEvento.nrRecibo', evtReintegr.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtReintegr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEvento.tpAmb', evtReintegr.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtReintegr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEvento.procEmi', evtReintegr.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtReintegr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEvento.verProc', evtReintegr.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtReintegr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEmpregador.tpInsc', evtReintegr.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtReintegr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideEmpregador.nrInsc', evtReintegr.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtReintegr.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideVinculo.cpfTrab', evtReintegr.ideVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtReintegr.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideVinculo.nisTrab', evtReintegr.ideVinculo.nisTrab.cdata, 1, '')
    if 'matricula' in dir(evtReintegr.ideVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.ideVinculo.matricula', evtReintegr.ideVinculo.matricula.cdata, 1, '')
    if 'tpReint' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.tpReint', evtReintegr.infoReintegr.tpReint.cdata, 1, '1;2;3;4;5;9')
    if 'nrProcJud' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.nrProcJud', evtReintegr.infoReintegr.nrProcJud.cdata, 0, '')
    if 'nrLeiAnistia' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.nrLeiAnistia', evtReintegr.infoReintegr.nrLeiAnistia.cdata, 0, '')
    if 'dtEfetRetorno' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.dtEfetRetorno', evtReintegr.infoReintegr.dtEfetRetorno.cdata, 1, '')
    if 'dtEfeito' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.dtEfeito', evtReintegr.infoReintegr.dtEfeito.cdata, 1, '')
    if 'indPagtoJuizo' in dir(evtReintegr.infoReintegr): validacoes_lista = validar_campo(validacoes_lista,'evtReintegr.infoReintegr.indPagtoJuizo', evtReintegr.infoReintegr.indPagtoJuizo.cdata, 1, 'S;N')
    return validacoes_lista