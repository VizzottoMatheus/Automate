
# ORIGEM DOS DADOS: http://siscomex.gov.br/


import requests
from io import BytesIO
import pandas as pd
from zipfile import ZipFile
import ssl
ssl._create_default_https_context = ssl._create_unverified_context




def exportacoes():
    """
    FUNÇÃO PARA EXTRAIR OS DADOS DE EXPORTAÇÃO E FAZER JOIN COM REFERÊNCIAS DE CÓDIGOS
    """

    # URLS
    x_path = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip"
    sh_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_SH.csv"
    ncm_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv"
    country_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv"
    unit_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_UNIDADE.csv"

    # LENDO ARQUIVO .ZIP
    r = requests.get(x_path, verify = False)
    files = ZipFile(BytesIO(r.content))
    arquivo_x = files.namelist()[0]
    exportacoes = pd.read_csv(files.open(arquivo_x), encoding="latin1", sep = ";")

    # CÓDIGOS
    sh = pd.read_csv(sh_path, sep = ";", encoding = "latin-1")
    sh_desc = sh[["CO_SH6", "NO_SH6_POR", "NO_SH4_POR", "NO_SH2_POR", "NO_SEC_POR"]]
    ncm = pd.read_csv(ncm_path, sep = ";", encoding = "latin-1")
    ncm_desc = ncm[["CO_NCM", "NO_NCM_POR", "CO_SH6"]]
    paises = pd.read_csv(country_path, sep = ";", encoding = "latin-1")
    paises_desc = paises[["CO_PAIS", "NO_PAIS"]]
    unidades = pd.read_csv(unit_path, sep = ";", encoding = "latin-1")


    # MERGE
    exportacoes2 = pd.merge(exportacoes, ncm_desc, on = "CO_NCM", how = "left")
    exportacoes3 = pd.merge(exportacoes2, paises_desc, on = "CO_PAIS", how = "left")
    exportacoes4 = pd.merge(exportacoes3, sh_desc, on = "CO_SH6", how = "left")
    exportacoes5 = pd.merge(exportacoes4, unidades, on = "CO_UNID", how = "left")

    return exportacoes5


def importacoes():
    """
    FUNÇÃO PARA EXTRAIR OS DADOS DE IMPORTAÇÃO E FAZER JOIN COM REFERÊNCIAS DE CÓDIGOS
    """

    # URLS
    m_path = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip"
    sh_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_SH.csv"
    ncm_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv"
    country_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv"
    unit_path = "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_UNIDADE.csv"

    # LENDO ARQUIVO .ZIP
    r = requests.get(m_path, verify = False)
    files = ZipFile(BytesIO(r.content))
    arquivo_x = files.namelist()[0]
    exportacoes = pd.read_csv(files.open(arquivo_x), encoding="latin1", sep = ";")

    # CÓDIGOS
    sh = pd.read_csv(sh_path, sep = ";", encoding = "latin-1")
    sh_desc = sh[["CO_SH6", "NO_SH6_POR", "NO_SH4_POR", "NO_SH2_POR", "NO_SEC_POR"]]
    ncm = pd.read_csv(ncm_path, sep = ";", encoding = "latin-1")
    ncm_desc = ncm[["CO_NCM", "NO_NCM_POR", "CO_SH6"]]
    paises = pd.read_csv(country_path, sep = ";", encoding = "latin-1")
    paises_desc = paises[["CO_PAIS", "NO_PAIS"]]
    unidades = pd.read_csv(unit_path, sep = ";", encoding = "latin-1")

    # MERGE
    exportacoes2 = pd.merge(exportacoes, ncm_desc, on = "CO_NCM", how = "left")
    exportacoes3 = pd.merge(exportacoes2, paises_desc, on = "CO_PAIS", how = "left")
    exportacoes4 = pd.merge(exportacoes3, sh_desc, on = "CO_SH6", how = "left")
    exportacoes5 = pd.merge(exportacoes4, unidades, on = "CO_UNID", how = "left")

    return exportacoes5