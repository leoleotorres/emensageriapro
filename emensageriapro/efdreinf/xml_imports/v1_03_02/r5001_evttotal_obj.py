#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql



def read_r5001_evttotal_obj(doc):
    r5001_evttotal_dados = {}
    r5001_evttotal_dados['versao'] = 'v1_03_02'
    r5001_evttotal_dados['status'] = 12
    r5001_evttotal_dados['identidade'] = doc.Reinf.evtTotal['id']
    r5001_evttotal_dados['processamento_codigo_resposta'] = 1
    evtTotal = doc.Reinf.evtTotal
    
    if 'perApur' in dir(evtTotal.ideEvento): r5001_evttotal_dados['perapur'] = evtTotal.ideEvento.perApur.cdata
    if 'tpInsc' in dir(evtTotal.ideContri): r5001_evttotal_dados['tpinsc'] = evtTotal.ideContri.tpInsc.cdata
    if 'nrInsc' in dir(evtTotal.ideContri): r5001_evttotal_dados['nrinsc'] = evtTotal.ideContri.nrInsc.cdata
    if 'cdRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): r5001_evttotal_dados['cdretorno'] = evtTotal.ideRecRetorno.ideStatus.cdRetorno.cdata
    if 'descRetorno' in dir(evtTotal.ideRecRetorno.ideStatus): r5001_evttotal_dados['descretorno'] = evtTotal.ideRecRetorno.ideStatus.descRetorno.cdata
    if 'nrProtEntr' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['nrprotentr'] = evtTotal.infoRecEv.nrProtEntr.cdata
    if 'dhProcess' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['dhprocess'] = evtTotal.infoRecEv.dhProcess.cdata
    if 'tpEv' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['tpev'] = evtTotal.infoRecEv.tpEv.cdata
    if 'idEv' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['idev'] = evtTotal.infoRecEv.idEv.cdata
    if 'hash' in dir(evtTotal.infoRecEv): r5001_evttotal_dados['hash'] = evtTotal.infoRecEv.hash.cdata
    if 'inclusao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 1
    elif 'alteracao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 2
    elif 'exclusao' in dir(evtTotal.infoTotal): r5001_evttotal_dados['operacao'] = 3
    #print dados
    insert = create_insert('r5001_evttotal', r5001_evttotal_dados)
    resp = executar_sql(insert, True)
    r5001_evttotal_id = resp[0][0]
    dados = r5001_evttotal_dados
    dados['evento'] = 'r5001'
    dados['id'] = r5001_evttotal_id
    dados['identidade_evento'] = doc.Reinf.evtTotal['id']
    dados['status'] = 1


    if 'regOcorrs' in dir(evtTotal.ideRecRetorno.ideStatus):
        for regOcorrs in evtTotal.ideRecRetorno.ideStatus.regOcorrs:
            r5001_regocorrs_dados = {}
            r5001_regocorrs_dados['r5001_evttotal_id'] = r5001_evttotal_id
            
            if 'tpOcorr' in dir(regOcorrs): r5001_regocorrs_dados['tpocorr'] = regOcorrs.tpOcorr.cdata
            if 'localErroAviso' in dir(regOcorrs): r5001_regocorrs_dados['localerroaviso'] = regOcorrs.localErroAviso.cdata
            if 'codResp' in dir(regOcorrs): r5001_regocorrs_dados['codresp'] = regOcorrs.codResp.cdata
            if 'dscResp' in dir(regOcorrs): r5001_regocorrs_dados['dscresp'] = regOcorrs.dscResp.cdata
            insert = create_insert('r5001_regocorrs', r5001_regocorrs_dados)
            resp = executar_sql(insert, True)
            r5001_regocorrs_id = resp[0][0]
            #print r5001_regocorrs_id

    if 'infoTotal' in dir(evtTotal):
        for infoTotal in evtTotal.infoTotal:
            r5001_infototal_dados = {}
            r5001_infototal_dados['r5001_evttotal_id'] = r5001_evttotal_id
            
            if 'nrRecArqBase' in dir(infoTotal): r5001_infototal_dados['nrrecarqbase'] = infoTotal.nrRecArqBase.cdata
            insert = create_insert('r5001_infototal', r5001_infototal_dados)
            resp = executar_sql(insert, True)
            r5001_infototal_id = resp[0][0]
            #print r5001_infototal_id

            if 'RTom' in dir(infoTotal):
                for RTom in infoTotal.RTom:
                    r5001_rtom_dados = {}
                    r5001_rtom_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'cnpjPrestador' in dir(RTom): r5001_rtom_dados['cnpjprestador'] = RTom.cnpjPrestador.cdata
                    if 'vlrTotalBaseRet' in dir(RTom): r5001_rtom_dados['vlrtotalbaseret'] = RTom.vlrTotalBaseRet.cdata
                    insert = create_insert('r5001_rtom', r5001_rtom_dados)
                    resp = executar_sql(insert, True)
                    r5001_rtom_id = resp[0][0]
                    #print r5001_rtom_id
        
            if 'RPrest' in dir(infoTotal):
                for RPrest in infoTotal.RPrest:
                    r5001_rprest_dados = {}
                    r5001_rprest_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'tpInscTomador' in dir(RPrest): r5001_rprest_dados['tpinsctomador'] = RPrest.tpInscTomador.cdata
                    if 'nrInscTomador' in dir(RPrest): r5001_rprest_dados['nrinsctomador'] = RPrest.nrInscTomador.cdata
                    if 'vlrTotalBaseRet' in dir(RPrest): r5001_rprest_dados['vlrtotalbaseret'] = RPrest.vlrTotalBaseRet.cdata
                    if 'vlrTotalRetPrinc' in dir(RPrest): r5001_rprest_dados['vlrtotalretprinc'] = RPrest.vlrTotalRetPrinc.cdata
                    if 'vlrTotalRetAdic' in dir(RPrest): r5001_rprest_dados['vlrtotalretadic'] = RPrest.vlrTotalRetAdic.cdata
                    if 'vlrTotalNRetPrinc' in dir(RPrest): r5001_rprest_dados['vlrtotalnretprinc'] = RPrest.vlrTotalNRetPrinc.cdata
                    if 'vlrTotalNRetAdic' in dir(RPrest): r5001_rprest_dados['vlrtotalnretadic'] = RPrest.vlrTotalNRetAdic.cdata
                    insert = create_insert('r5001_rprest', r5001_rprest_dados)
                    resp = executar_sql(insert, True)
                    r5001_rprest_id = resp[0][0]
                    #print r5001_rprest_id
        
            if 'RRecRepAD' in dir(infoTotal):
                for RRecRepAD in infoTotal.RRecRepAD:
                    r5001_rrecrepad_dados = {}
                    r5001_rrecrepad_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'cnpjAssocDesp' in dir(RRecRepAD): r5001_rrecrepad_dados['cnpjassocdesp'] = RRecRepAD.cnpjAssocDesp.cdata
                    if 'vlrTotalRep' in dir(RRecRepAD): r5001_rrecrepad_dados['vlrtotalrep'] = RRecRepAD.vlrTotalRep.cdata
                    if 'CRRecRepAD' in dir(RRecRepAD): r5001_rrecrepad_dados['crrecrepad'] = RRecRepAD.CRRecRepAD.cdata
                    if 'vlrCRRecRepAD' in dir(RRecRepAD): r5001_rrecrepad_dados['vlrcrrecrepad'] = RRecRepAD.vlrCRRecRepAD.cdata
                    if 'vlrCRRecRepADSusp' in dir(RRecRepAD): r5001_rrecrepad_dados['vlrcrrecrepadsusp'] = RRecRepAD.vlrCRRecRepADSusp.cdata
                    insert = create_insert('r5001_rrecrepad', r5001_rrecrepad_dados)
                    resp = executar_sql(insert, True)
                    r5001_rrecrepad_id = resp[0][0]
                    #print r5001_rrecrepad_id
        
            if 'RComl' in dir(infoTotal):
                for RComl in infoTotal.RComl:
                    r5001_rcoml_dados = {}
                    r5001_rcoml_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'CRComl' in dir(RComl): r5001_rcoml_dados['crcoml'] = RComl.CRComl.cdata
                    if 'vlrCRComl' in dir(RComl): r5001_rcoml_dados['vlrcrcoml'] = RComl.vlrCRComl.cdata
                    if 'vlrCRComlSusp' in dir(RComl): r5001_rcoml_dados['vlrcrcomlsusp'] = RComl.vlrCRComlSusp.cdata
                    insert = create_insert('r5001_rcoml', r5001_rcoml_dados)
                    resp = executar_sql(insert, True)
                    r5001_rcoml_id = resp[0][0]
                    #print r5001_rcoml_id
        
            if 'RCPRB' in dir(infoTotal):
                for RCPRB in infoTotal.RCPRB:
                    r5001_rcprb_dados = {}
                    r5001_rcprb_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'CRCPRB' in dir(RCPRB): r5001_rcprb_dados['crcprb'] = RCPRB.CRCPRB.cdata
                    if 'vlrCRCPRB' in dir(RCPRB): r5001_rcprb_dados['vlrcrcprb'] = RCPRB.vlrCRCPRB.cdata
                    if 'vlrCRCPRBSusp' in dir(RCPRB): r5001_rcprb_dados['vlrcrcprbsusp'] = RCPRB.vlrCRCPRBSusp.cdata
                    insert = create_insert('r5001_rcprb', r5001_rcprb_dados)
                    resp = executar_sql(insert, True)
                    r5001_rcprb_id = resp[0][0]
                    #print r5001_rcprb_id
        
            if 'RRecEspetDesp' in dir(infoTotal):
                for RRecEspetDesp in infoTotal.RRecEspetDesp:
                    r5001_rrecespetdesp_dados = {}
                    r5001_rrecespetdesp_dados['r5001_infototal_id'] = r5001_infototal_id
                    
                    if 'CRRecEspetDesp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados['crrecespetdesp'] = RRecEspetDesp.CRRecEspetDesp.cdata
                    if 'vlrReceitaTotal' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados['vlrreceitatotal'] = RRecEspetDesp.vlrReceitaTotal.cdata
                    if 'vlrCRRecEspetDesp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados['vlrcrrecespetdesp'] = RRecEspetDesp.vlrCRRecEspetDesp.cdata
                    if 'vlrCRRecEspetDespSusp' in dir(RRecEspetDesp): r5001_rrecespetdesp_dados['vlrcrrecespetdespsusp'] = RRecEspetDesp.vlrCRRecEspetDespSusp.cdata
                    insert = create_insert('r5001_rrecespetdesp', r5001_rrecespetdesp_dados)
                    resp = executar_sql(insert, True)
                    r5001_rrecespetdesp_id = resp[0][0]
                    #print r5001_rrecespetdesp_id
        
    return dados