from fastapi import FastAPI
from pydantic import BaseModel

# Criação da aplicação
app = FastAPI(
    title="Sistema 4.0 de Curitiba",
    description="API do sistema para monitoramento e previsão de trânsito, transporte, clima, segurança e saúde",
    version="0.1.0"
)

# Endpoint de teste de funcionamento
@app.get("/saudacao")
def saudacao():
    return {"mensagem": "API do Sistema 4.0 de Curitiba funcionando!"}

# Modelo de exemplo para previsão de trânsito
class ConsultaTransito(BaseModel):
    latitude: float
    longitude: float
    horizonte_minutos: int = 30

@app.post("/prever/transito")
def prever_transito(consulta: ConsultaTransito):
    # Aqui ainda não existe modelo de IA — isso é um exemplo
    return {
        "previsao": 42,
        "unidade": "veículos/minuto",
        "horizonte_minutos": consulta.horizonte_minutos,
        "observacao": "modelo ainda não treinado (exemplo)"
    }

