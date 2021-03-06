#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_r3010_evtespdesportivo(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.Reinf['xmlns'].split('/')
    evtEspDesportivo = doc.Reinf.evtEspDesportivo
    
    if 'indRetif' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.indRetif', evtEspDesportivo.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.nrRecibo', evtEspDesportivo.ideEvento.nrRecibo.cdata, 0, '')
    if 'dtApuracao' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.dtApuracao', evtEspDesportivo.ideEvento.dtApuracao.cdata, 1, '')
    if 'tpAmb' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.tpAmb', evtEspDesportivo.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.procEmi', evtEspDesportivo.ideEvento.procEmi.cdata, 1, '1;2')
    if 'verProc' in dir(evtEspDesportivo.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideEvento.verProc', evtEspDesportivo.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtEspDesportivo.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.tpInsc', evtEspDesportivo.ideContri.tpInsc.cdata, 1, '1;2')
    if 'nrInsc' in dir(evtEspDesportivo.ideContri): validacoes_lista = validar_campo(validacoes_lista,'evtEspDesportivo.ideContri.nrInsc', evtEspDesportivo.ideContri.nrInsc.cdata, 1, '')
    if 'ideEstab' in dir(evtEspDesportivo.ideContri):
        for ideEstab in evtEspDesportivo.ideContri.ideEstab:
            
            if 'tpInscEstab' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.tpInscEstab', ideEstab.tpInscEstab.cdata, 1, '1')
            if 'nrInscEstab' in dir(ideEstab): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.nrInscEstab', ideEstab.nrInscEstab.cdata, 1, '')
            if 'vlrReceitaTotal' in dir(ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.receitaTotal.vlrReceitaTotal', ideEstab.receitaTotal.vlrReceitaTotal.cdata, 1, '')
            if 'vlrCP' in dir(ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.receitaTotal.vlrCP', ideEstab.receitaTotal.vlrCP.cdata, 1, '')
            if 'vlrCPSuspTotal' in dir(ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.receitaTotal.vlrCPSuspTotal', ideEstab.receitaTotal.vlrCPSuspTotal.cdata, 0, '')
            if 'vlrReceitaClubes' in dir(ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.receitaTotal.vlrReceitaClubes', ideEstab.receitaTotal.vlrReceitaClubes.cdata, 1, '')
            if 'vlrRetParc' in dir(ideEstab.receitaTotal): validacoes_lista = validar_campo(validacoes_lista,'ideEstab.receitaTotal.vlrRetParc', ideEstab.receitaTotal.vlrRetParc.cdata, 1, '')


            if 'boletim' in dir(ideEstab):
                for boletim in ideEstab.boletim:
                    
                    if 'nrBoletim' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nrBoletim', boletim.nrBoletim.cdata, 1, '')
                    if 'tpCompeticao' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.tpCompeticao', boletim.tpCompeticao.cdata, 1, '1;2')
                    if 'categEvento' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.categEvento', boletim.categEvento.cdata, 1, '1;2;3;4')
                    if 'modDesportiva' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.modDesportiva', boletim.modDesportiva.cdata, 1, '')
                    if 'nomeCompeticao' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nomeCompeticao', boletim.nomeCompeticao.cdata, 1, '')
                    if 'cnpjMandante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.cnpjMandante', boletim.cnpjMandante.cdata, 1, '')
                    if 'cnpjVisitante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.cnpjVisitante', boletim.cnpjVisitante.cdata, 0, '')
                    if 'nomeVisitante' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.nomeVisitante', boletim.nomeVisitante.cdata, 0, '')
                    if 'pracaDesportiva' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.pracaDesportiva', boletim.pracaDesportiva.cdata, 1, '')
                    if 'codMunic' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.codMunic', boletim.codMunic.cdata, 0, '')
                    if 'uf' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.uf', boletim.uf.cdata, 1, '')
                    if 'qtdePagantes' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.qtdePagantes', boletim.qtdePagantes.cdata, 1, '')
                    if 'qtdeNaoPagantes' in dir(boletim): validacoes_lista = validar_campo(validacoes_lista,'boletim.qtdeNaoPagantes', boletim.qtdeNaoPagantes.cdata, 1, '')
        
        
            if 'infoProc' in dir(ideEstab.receitaTotal):
                for infoProc in ideEstab.receitaTotal.infoProc:
                    
                    if 'tpProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.tpProc', infoProc.tpProc.cdata, 1, '1;2')
                    if 'nrProc' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.nrProc', infoProc.nrProc.cdata, 1, '')
                    if 'codSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.codSusp', infoProc.codSusp.cdata, 0, '')
                    if 'vlrCPSusp' in dir(infoProc): validacoes_lista = validar_campo(validacoes_lista,'infoProc.vlrCPSusp', infoProc.vlrCPSusp.cdata, 1, '')
        
        
    return validacoes_lista