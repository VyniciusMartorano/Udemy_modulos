from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


meu_email = 'vyniciusmartorano26@gmail.com'
minha_senha = ''

#pessoa que envia
seu_nome = 'Vynicius Martorano'
cabeçalho = 'Este é um E-mail de testes'

#destinatario
destinatario = ''
nome_destinatario = 'Vynicius Salusto'




with open('template.html','r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(texto=f'Olá {nome_destinatario},'
                                               f' Esta é uma mensagem '
                                               f'programada. Data atual:'
                                               f'{data_atual}')#safe_substitute serve pra nao levantar
                                                                        #excessoes se a variavel nao for atribuida
                                                                         #a um valor


msg = MIMEMultipart()
msg['from'] = seu_nome
msg['to'] = destinatario
msg['subject'] = cabeçalho


corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)   #anexar mensagem html ao email


with open('teclado.jpg','rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img) #anexar imagem ao email


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)  #enviar mensagem
        print('E-mail enviado com sucesso')
    except Exception as erro:
        print('E-mail não enviado...')
        print(f'Erro: {erro}')


