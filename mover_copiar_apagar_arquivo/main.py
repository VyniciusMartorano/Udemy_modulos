import os
import shutil

caminho_original = 'D:\prints'
caminho_novo = 'D:\prints2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print('O arquivo ja existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #se o arquivo for '.png' apague-o
        if '.png' in file:
            os.remove(new_file_path)
            print(f'{new_file_path} apagado com sucesso')


        '''
        mover arquivos de old_file_path para new_file_path
        if '.png' in file:  #se o arquivo for .png mova-os
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} movido para com sucesso!')'''


        '''
        copiar arquivos de old_file_pach para _new_file_path
        if '.png' in file:
            shutil.copy(old_file_path, new_file_path)
            print('Arquivo copiado com sucesso')'''
