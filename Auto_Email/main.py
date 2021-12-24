from string import Template
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib

from Auto_Email.Info_email import *

cabecalho = 'Este é um E-mail de testes!'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(texto=f'Olá {nome_destinatario}, Segue planilha de Josefa Salusto.\n{msg_principal}')

msg = MIMEMultipart()
msg['from'] = seu_nome
msg['to'] = email_destinatario
msg['subject'] = cabecalho

corpo = MIMEText(corpo_msg,'html')
msg.attach(corpo)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(my_email, my_password)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Houve um erro ao enviar seu E-mail.')
        print(f'Erro: {e}')




