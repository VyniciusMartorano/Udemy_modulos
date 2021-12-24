"""
pip install pypdf2
Documentação:
https://pythonhosted.org/PyPDF2/
"""
import PyPDF2
import os


"""
#JUNTAR 2 PDFS EM 1

caminho_dos_pdfs = 
novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)


with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf','wb') as  meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""


"""
DIVIDIR UM PDF EM 2 PELA QUANTIDADE DE PAGINAS

with open(r'C:\Users\vynic\PycharmProjects\UdemyModulos\PyPDF2\pdfs\novo_arquivo.pdf','rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()


    for num_pagina in range(0,num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'C:/Users/vynic/PycharmProjects/UdemyModulos/PyPDF2/novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
"""


















