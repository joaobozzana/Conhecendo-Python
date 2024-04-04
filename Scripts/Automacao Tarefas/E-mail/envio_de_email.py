from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

# Dados de acesso dos emails
email_senha = open('pass', 'r').read() # Carrega a senha do arquivo 'pass', que contém a senha gerada para o email remetente
email_origem = 'XXXXX@gmail.com' # # Endereço de email remetente
email_destino = ('XXXXX@gmail.com') # Endereço de email(s) de destino (pode ser uma lista de destinatários)


# Textos do email
assunto = 'Nome do Assunto1' # Assunto do email
body = open('corpo_email_html.txt', 'r').read() # Corpo do email (HTML ou texto) // # Use 'corpo_email.txt' para corpo de texto simples


# Variável para simplificar as chamadas posteriores da função 'EmailMessage()'
mensagem = EmailMessage()


#Enviar anexo
anexo_path = 'teste,jpg' # Em caso de envio de PDF só por o nome_do_arquivo.pdf
mime_type, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')


# Define os cabeçalhos do email
mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto


# Estruturação do email (se o corpo do email for do tipo html, incluir o parâmetro subtype='html', ao lado do parâmetro body.
mensagem.set_content(body, subtype='html') # Tire subtype='html' se for usar o corpo de texto simples .txt


# Adiciona SSL ao código para garantir a segurança dos dados
safe = ssl.create_default_context()


# Adiciona o arquivo anexo ao email
with open(anexo_path, 'rb') as ap:
     mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                            filename=os.path.basename(anexo_path))
     
# Acesso e envio do email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
