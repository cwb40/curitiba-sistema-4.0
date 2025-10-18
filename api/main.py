# Arquivo: main.py
# API principal do sistema Curitiba 4.0

from fastapi import FastAPI
from clima import obter_clima

app = FastAPI(title="Curitiba Sistema 4.0")

@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo à API Curitiba 4.0"}

@app.get("/clima")
def rota_clima():
    """Rota que mostra o clima atual de Curitiba"""
    return obter_clima()

