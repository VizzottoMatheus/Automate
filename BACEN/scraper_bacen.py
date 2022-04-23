import pandas as pd

def bacen_downloader(date_as_index = False):
    api_sgs = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=csv"
    inputs = {
        'Dólar': 1,
        'Euro': 21619,
        'Libra': 21623,
        'Índice nacional de preços ao consumidor-amplo (IPCA)': 433,
        'Índice geral de preços do mercado (IGP-M)': 189,
        'Índice de Preços por Atacado-Mercado (IPA-M)': 7450,
        'Índice nacional de custo da construção (INCC)': 192,
        'SELIC': 432,
        'Índice de Atividade Econômica do Banco Central com ajuste sazonal (IBC-BR)': 24364,
        'Índice de Atividade Econômica Regional - Região Sul - com ajuste sazonal (IBC-SUL)': 25403,
        'Saldo da carteira de crédito em relação ao PIB': 20622,
        'Saldo da carteira de crédito com recursos livres a pessoas jurídicas em relação ao PIB': 20626,
        'Saldo da carteira de crédito com recursos livres a pessoas físicas em relação ao PIB': 20627,
        'Saldo da carteira de crédito com recursos direcionados a pessoas jurídicas em relação ao PIB': 20629,
        'Saldo da carteira de crédito com recursos direcionados a pessoas físicas em relação ao PIB': 20630,
        'Saldo da carteira de crédito a pessoas jurídicas em relação ao PIB': 20623,
        'Saldo da carteira de crédito a pessoas físicas em relação ao PIB': 20624
        }
    print("Baixando dados...")
    d = {}
    for serie, codigo in inputs.items():
        #print(f" -{serie}")
        link = api_sgs.format(codigo)
        if date_as_index == False:
            d["{}".format(serie)] = pd.read_csv(link, sep = ";", decimal= ",", dtype = {"valor": "float"}, parse_dates = ["data"])
        elif date_as_index == True:
            d["{}".format(serie)] = pd.read_csv(link, sep = ";", decimal= ",", dtype = {"valor": "float"}, parse_dates = ["data"], index_col = ["data"]).sort_index()
    print("Dados baixados e salvos em formato de dicionário.")
    return d
