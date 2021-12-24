"""
Java Script Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de facil utilização. muito utilizado por APIs
"""
import json
from JSON.dados import clientes

with open('clientes.json', 'w') as arquivo:
    json.dump(clientes, arquivo, indent=4)
with open('clientes.json','r') as arquivo:
    dados = json.load(arquivo)  #transforma o arquivo de volta a sua forma original
    for key, value in dados.items():
        print(key)
        print(value)