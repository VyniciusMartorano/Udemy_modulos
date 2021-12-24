import os

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho <peta:
        tamanho /= tera
        texto = 'T'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


caminho_procura = fr"C:\Users\vynic\Downloads"
termo_procura = str(input('Digite um termo: ')).strip()
conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        try:
            if termo_procura in arquivo:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                #divide o arquivo em nome e extensão
                nome_arquivo, extensão_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo) #tamanho arquivo em bytes
                print()
                print(f'Encontrei o arquivo: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {extensão_arquivo}')
                print(f'Tamanho: {formata_tamanho(tamanho)}')
        except PermissionError as e:
            print('Sem permissoes nesse arquivo')
        except FileNotFoundError as e:
            print('Não achei oque voce procura :(')
        except Exception as e:
            print('Erro Desconhecido', e)
print()
print(f'{conta} arquivo(s) encontrado(s)')