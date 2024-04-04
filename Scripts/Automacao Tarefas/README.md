# Scripts

## Organizador de Arquivos

A função do script [OrganizadorDeArquivos.py](/Scripts/Automacao%20Tarefas/Organizar%20pastas/OrganizadorDeArquivos.py) é percorrer uma pasta selecionada pelo usuário e organizar os arquivos em subpastas com base em suas extensões. A fins de teste, o script esta para percorrer a pasta Downloads e separar arquivos .jpeg e .zip. Para gerar uma automatização basta usar/configurar o **crontab** para Linux/MAC ou o **Agendador de Tarefas** no caso de Windows para que a axecução do script ocorra de tempos em tempos (de acordo com a própria configuração).

## Envio de e-mails

A intenção inicial foi explorar e entender as bibliotecas **email.message**, **smtplib**, **ssl**, **mimetypes** e **imbox**, além de aprender a enviar e ler e-mails por meio de programação. Embora os scripts tenham sido desenvolvidos de forma simplificada, apenas para exploração e compreensão das funcionalidades, fica evidente o potencial significativo para expandir esses conceitos em projetos mais complexos.

O script [envio_de_email.py](/Scripts/Automacao%20Tarefas/E-mail/envio_de_email.py) foi criado com o propósito específico de enviar e-mails, enquanto o script [ler_email.py](/Scripts/Automacao%20Tarefas/E-mail/ler_email.py) foi desenvolvido para ler e-mails, permitindo a extração de informações como título, corpo, remetente e até mesmo o download de arquivos anexados ao e-mail. Essas capacidades oferecem uma base sólida para integração em projetos de automação de tarefas ou sistemas mais amplos.
