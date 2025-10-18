# Arquivo: clima.py
# Faz a conexão com a API do OpenWeatherMap e retorna dados de clima

import requests
from .configuracoes import API_CHAVE, URL_CLIMA, CIDADE

def obter_clima():
    """Busca dados atuais do clima de Curitiba."""
    parametros = {
        "q": CIDADE,
        "appid": API_CHAVE,
        "units": "metric",
        "lang": "pt_br"
    }
    resposta = requests.get(URL_CLIMA, params=parametros)
    dados = resposta.json()

    if resposta.status_code != 200:
        return {"erro": "Não foi possível obter os dados de clima."}

    resultado = {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
        "umidade": dados["main"]["humidity"],
        "descricao": dados["weather"][0]["description"]
    }

    return resultado
