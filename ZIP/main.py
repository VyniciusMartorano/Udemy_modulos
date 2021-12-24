from zipfile import ZipFile
import os

caminho = r'D:\prints'

with ZipFile('arquivo.zip','w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho,arquivo)
        zip.write(caminho_completo) #escreve tudo que ta em caminho completo
                                    #em 'arquivos.zip'

with ZipFile('arquivo.zip','r') as zip:
    for arquivo in zip.namelist():  #ler o que tem no arquivo zip
        print(arquivo)

with ZipFile('arquivo.zip','r') as zip:
    zip.extractall('Descompactado')

