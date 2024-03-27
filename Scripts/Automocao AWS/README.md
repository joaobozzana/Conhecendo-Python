# Scripts na AWS

A ideia é explorar os serviços da AWS, de forma que os scripts (funções lambda) automatizem alguns serviços. Todo o desenvolvimento será sempre limitado ao que a AWS oferece gratuitamente. Além disso, quaisquer chaves que possam aparecer estão **desativadas**.

## Script para criar instâncias EC2

Um dos serviços oferecidos pela AWS é o Amazon EC2, que possibilita a criação de máquinas virtuais, ou instâncias, que operam na Nuvem AWS. Minha primeira [função Lambda](/Scripts/Automocao%20AWS/Create-EC2-t2micro-linux.py) visa automatizar a criação dessas instâncias, permitindo configurar diversos aspectos, como imagem, tipo de instância, entre outros, de acordo com as preferências desejadas.

- AMI = ami-0d5ae304a0b933620 
    - O modelo da maquina "Amazon Linux 2023 AMI" gratuito
- INSTANCE_TYPE = t2.micro 
    - Que é o tipo de instância gratuita
- KEY_NAME = ec2-script 
    - par de chaves criado
- SUBNET_ID = subnet-0f9d97a5eb1a60234 
    - 173.31.0.0/20

Algumas capturas de tela do processo:

- Função lambda:

    ![Função](/Scripts/Automocao%20AWS/imgs%20Create/funcao-EC2.png)

- Instância criada:

    ![Instância gerada](/Scripts/Automocao%20AWS/imgs%20Create/instancia-EC2.png)

- Detalhes da instância:

    ![Detalhes da Instância 1/2](/Scripts/Automocao%20AWS/imgs%20Create/detalhes-1-EC2.png)

    ![Detalhes da Instância 2/2](/Scripts/Automocao%20AWS/imgs%20Create/detalhes-2-EC2.png)


## Script fazer backups de instâncias EC2

Seguindo a mesma linha de raciocínio da ideia anterior, na qual automatizei a criação de instâncias EC2, desta vez concentrei-me na automatização dos Snapshots (backup). Para isso, desenvolvi uma [função Lambda](/Scripts/Automocao%20AWS/Backup-EC2.py) e utilizei o recurso **Amazon EventBridge**. Através dele, programei a frequência com que desejo que minha função seja executada, garantindo assim a criação de novos Snapshots de forma regular.

A programação do **Amazon EventBridge**, se deu da seguinte forma:

- Criação do novo cronograma:

    ![Criação](/Scripts/Automocao%20AWS/imgs%20Backup/criacao-Bridge.png)

- Para o tipo de cronograma, optei por utilizar intervalos como base, que é mais simples para o teste.

    ![Tipo de cronograma](/Scripts/Automocao%20AWS/imgs%20Backup/intervalo-Bridge.png)

- Nas opções disponíveis, seleciono o serviço Lambda e escolho a função desejada.

    ![Lambda](/Scripts/Automocao%20AWS/imgs%20Backup/escolha-1-Bridge.png)

    ![Lambda](/Scripts/Automocao%20AWS/imgs%20Backup/escolha-2-Bridge.png)

Para completar, incluí imagens da minha instância, dos snapshots gerados e do log que demonstra o script navegando por todas as regiões e realizando o backup de qualquer instância que encontre.

- ![Instância](/Scripts/Automocao%20AWS/imgs%20Backup/instancia.png)

- ![snapshots](/Scripts/Automocao%20AWS/imgs%20Backup/snapshots.png)

- ![log](/Scripts/Automocao%20AWS/imgs%20Backup/logs.png)