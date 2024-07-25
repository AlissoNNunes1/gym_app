# controllers.py
import json

def salvar_dados(usuario, filename="dados.json"):
    with open(filename, 'w') as f:
        json.dump(usuario, f, default=lambda o: o.__dict__)

def carregar_dados(filename="dados.json"):
    with open(filename, 'r') as f:
        dados = json.load(f)
        return dados
