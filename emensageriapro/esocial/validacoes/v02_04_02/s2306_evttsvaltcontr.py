#coding:utf-8
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2306_evttsvaltcontr(arquivo):
    from emensageriapro.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTSVAltContr = doc.eSocial.evtTSVAltContr
    
    if 'indRetif' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.indRetif', evtTSVAltContr.ideEvento.indRetif.cdata, 1, '1;2')
    if 'nrRecibo' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.nrRecibo', evtTSVAltContr.ideEvento.nrRecibo.cdata, 0, '')
    if 'tpAmb' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.tpAmb', evtTSVAltContr.ideEvento.tpAmb.cdata, 1, '1;2')
    if 'procEmi' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.procEmi', evtTSVAltContr.ideEvento.procEmi.cdata, 1, '1;2;3;4;5')
    if 'verProc' in dir(evtTSVAltContr.ideEvento): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEvento.verProc', evtTSVAltContr.ideEvento.verProc.cdata, 1, '')
    if 'tpInsc' in dir(evtTSVAltContr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEmpregador.tpInsc', evtTSVAltContr.ideEmpregador.tpInsc.cdata, 1, '1;2;3;4')
    if 'nrInsc' in dir(evtTSVAltContr.ideEmpregador): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideEmpregador.nrInsc', evtTSVAltContr.ideEmpregador.nrInsc.cdata, 1, '')
    if 'cpfTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.cpfTrab', evtTSVAltContr.ideTrabSemVinculo.cpfTrab.cdata, 1, '')
    if 'nisTrab' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.nisTrab', evtTSVAltContr.ideTrabSemVinculo.nisTrab.cdata, 0, '')
    if 'codCateg' in dir(evtTSVAltContr.ideTrabSemVinculo): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.ideTrabSemVinculo.codCateg', evtTSVAltContr.ideTrabSemVinculo.codCateg.cdata, 1, '101;102;103;104;105;106;111;201;202;301;302;303;305;306;307;308;309;401;410;701;711;712;721;722;723;731;734;738;741;751;761;771;781;901;902;903;904;905')
    if 'dtAlteracao' in dir(evtTSVAltContr.infoTSVAlteracao): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.infoTSVAlteracao.dtAlteracao', evtTSVAltContr.infoTSVAlteracao.dtAlteracao.cdata, 1, '')
    if 'natAtividade' in dir(evtTSVAltContr.infoTSVAlteracao): validacoes_lista = validar_campo(validacoes_lista,'evtTSVAltContr.infoTSVAlteracao.natAtividade', evtTSVAltContr.infoTSVAlteracao.natAtividade.cdata, 0, '1;2')
    if 'infoComplementares' in dir(evtTSVAltContr.infoTSVAlteracao):
        for infoComplementares in evtTSVAltContr.infoTSVAlteracao.infoComplementares:
            

            if 'cargoFuncao' in dir(infoComplementares):
                for cargoFuncao in infoComplementares.cargoFuncao:
                    
                    if 'codCargo' in dir(cargoFuncao): validacoes_lista = validar_campo(validacoes_lista,'cargoFuncao.codCargo', cargoFuncao.codCargo.cdata, 1, '')
                    if 'codFuncao' in dir(cargoFuncao): validacoes_lista = validar_campo(validacoes_lista,'cargoFuncao.codFuncao', cargoFuncao.codFuncao.cdata, 0, '')
        
            if 'remuneracao' in dir(infoComplementares):
                for remuneracao in infoComplementares.remuneracao:
                    
                    if 'vrSalFx' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.vrSalFx', remuneracao.vrSalFx.cdata, 1, '')
                    if 'undSalFixo' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.undSalFixo', remuneracao.undSalFixo.cdata, 1, '1;2;3;4;5;6;7')
                    if 'dscSalVar' in dir(remuneracao): validacoes_lista = validar_campo(validacoes_lista,'remuneracao.dscSalVar', remuneracao.dscSalVar.cdata, 0, '')
        
            if 'infoEstagiario' in dir(infoComplementares):
                for infoEstagiario in infoComplementares.infoEstagiario:
                    
                    if 'natEstagio' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.natEstagio', infoEstagiario.natEstagio.cdata, 1, 'O;N')
                    if 'nivEstagio' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nivEstagio', infoEstagiario.nivEstagio.cdata, 1, '1;2;3;4;8;9')
                    if 'areaAtuacao' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.areaAtuacao', infoEstagiario.areaAtuacao.cdata, 0, '')
                    if 'nrApol' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nrApol', infoEstagiario.nrApol.cdata, 0, '')
                    if 'vlrBolsa' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.vlrBolsa', infoEstagiario.vlrBolsa.cdata, 0, '')
                    if 'dtPrevTerm' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.dtPrevTerm', infoEstagiario.dtPrevTerm.cdata, 1, '')
                    if 'cnpjInstEnsino' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.cnpjInstEnsino', infoEstagiario.cnpjInstEnsino.cdata, 0, '')
                    if 'nmRazao' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nmRazao', infoEstagiario.nmRazao.cdata, 1, '')
                    if 'dscLograd' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.dscLograd', infoEstagiario.dscLograd.cdata, 0, '')
                    if 'nrLograd' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.nrLograd', infoEstagiario.nrLograd.cdata, 0, '')
                    if 'bairro' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.bairro', infoEstagiario.bairro.cdata, 0, '')
                    if 'cep' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.cep', infoEstagiario.cep.cdata, 0, '')
                    if 'codMunic' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.codMunic', infoEstagiario.codMunic.cdata, 0, '')
                    if 'uf' in dir(infoEstagiario): validacoes_lista = validar_campo(validacoes_lista,'infoEstagiario.uf', infoEstagiario.uf.cdata, 0, '')
        
    return validacoes_lista