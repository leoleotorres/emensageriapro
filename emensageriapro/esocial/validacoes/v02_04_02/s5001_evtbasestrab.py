#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s5001_evtbasestrab(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtBasesTrab = doc.eSocial.evtBasesTrab
    
    if 'nrRecArqBase' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.nrRecArqBase', evtBasesTrab.ideEvento.nrRecArqBase.cdata, 0, '')
    if 'indApuracao' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.indApuracao', evtBasesTrab.ideEvento.indApuracao.cdata, 1, '1;2')
    if 'perApur' in dir(evtBasesTrab.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEvento.perApur', evtBasesTrab.ideEvento.perApur.cdata, 1, '')
    if 'tpInsc' in dir(evtBasesTrab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEmpregador.tpInsc', evtBasesTrab.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtBasesTrab.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideEmpregador.nrInsc', evtBasesTrab.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtBasesTrab.ideTrabalhador): validacoes_lista = validar_campo(validacoes_lista,'evtBasesTrab.ideTrabalhador.cpfTrab', evtBasesTrab.ideTrabalhador.cpfTrab.cdata, 1, '')
    if 'procJudTrab' in dir(evtBasesTrab.ideTrabalhador):
        for procJudTrab in evtBasesTrab.ideTrabalhador.procJudTrab:
            
            if 'nrProcJud' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.nrProcJud', procJudTrab.nrProcJud.cdata, 1, '')
            if 'codSusp' in dir(procJudTrab): validacoes_lista = validar_campo(validacoes_lista,'procJudTrab.codSusp', procJudTrab.codSusp.cdata, 1, '')

    if 'infoCpCalc' in dir(evtBasesTrab):
        for infoCpCalc in evtBasesTrab.infoCpCalc:
            
            if 'tpCR' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.tpCR', infoCpCalc.tpCR.cdata, 1, '108201;108202;108203;108204;108221;108222;108223;108224;109901;109902')
            if 'vrCpSeg' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.vrCpSeg', infoCpCalc.vrCpSeg.cdata, 1, '')
            if 'vrDescSeg' in dir(infoCpCalc): validacoes_lista = validar_campo(validacoes_lista,'infoCpCalc.vrDescSeg', infoCpCalc.vrDescSeg.cdata, 1, '')

    if 'infoCp' in dir(evtBasesTrab):
        for infoCp in evtBasesTrab.infoCp:
            

            if 'ideEstabLot' in dir(infoCp):
                for ideEstabLot in infoCp.ideEstabLot:
                    
                    if 'tpInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.tpInsc', ideEstabLot.tpInsc.cdata, 1, '1;2;3;4')
                    if 'nrInsc' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.nrInsc', ideEstabLot.nrInsc.cdata, 1, '')
                    if 'codLotacao' in dir(ideEstabLot): validacoes_lista = validar_campo(validacoes_lista,'ideEstabLot.codLotacao', ideEstabLot.codLotacao.cdata, 1, '')
        
    return validacoes_lista