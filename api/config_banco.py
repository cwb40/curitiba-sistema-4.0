import sqlite3
import os

CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), 'dados', 'banco.db')

def criar_banco():
    if not os.path.exists(os.path.dirname(CAMINHO_BANCO)):
        os.makedirs(os.path.dirname(CAMINHO_BANCO))

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()
