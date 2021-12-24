"""
https://openpyxl.readthedocs.io/en/stable/
pip install openpyxl
pipenv install openpyxl
"""
import openpyxl

pedidos = openpyxl.load_workbook(r'C:\Users\vynic\PycharmProjects\UdemyModulos\Ler_planilhas_excel\Nova_planilha.xlsx')
nome_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']
planilha1['c2'] = 89.90
planilha1['b2'] = 2070
pedidos.save('Nova_planilha.xlsx')   #salvar um novo arquivo


for linha in planilha1:
    if linha[0].value is not None:
        print(linha[0].value, end=' ')
    if linha[1].value is not None:
        print(linha[1].value, end=' ')
    if linha[2].value is not None:
        print(linha[2].value)