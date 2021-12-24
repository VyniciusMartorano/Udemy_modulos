"""
Comma Separated Values - CSV (Valores separados por virgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('dados.csv','r') as arquivo:
    #dados = csv.reader(arquivo)   #apenas ler o arquivo
    dados = csv.DictReader(arquivo) #transformar os dados em dicionarios
        #dados é um iterador, logo para pular a primeira linha eu usei o next
    for dado in dados:
        print(dado['Nome'],dado['Sobrenome'])
        print(f'Telefone: {dado["Telefone"]}')
        print()
