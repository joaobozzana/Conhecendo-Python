from imbox import Imbox 
from datetime import datetime
import pandas as pd

username = 'email_que_gerou_a_senha@gmail.com'
password = open('pass', 'r').read()
host = 'imap.gmail.com' # servidor imap do gmail

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages() # Posso passar filtros por ai

download_folder = 'attachments'

for (uid, message) in messages:
    print(message.subject) # Titulo do email
    print(message.body) # Corpo do email
    print(message.sent_from) # De quem foi mandado
    print(message.sent_to) # Pra quem foi enviado
    print(message.cc) # CC
    print(message.headers) # Cabeçalho da mensagem
    print(message.date) # Data que foi enviada
    print(message.attachments) # Vejo se tem anexo

    for attach in message.attachments:
        file = open('attachments/arquivo.rtf', 'wb') # Para baixar o arquivo no pc tem que por a extenção correta.
        attach['content'].seek(0)
        file.write(attach['content'].read())
        file.close()
    break