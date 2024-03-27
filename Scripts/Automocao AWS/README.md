# Scripts na AWS

Aqui, colocarei scripts focados na plataforma da AWS. Todo o desenvolvimento será sempre limitado ao que a AWS oferece gratuitamente. Além disso, quaisquer chaves que possam aparecer estão **desativadas**.

## Script para criar maquinas EC2

Neste [script](/Scripts/Automocao%20AWS/Create-EC2-t2micro-linux.py), desenvolvi uma função lambda para a criação automática de instâncias EC2. Utilizei variáveis de ambiente para passar as definições desejadas para a instância, sendo elas:

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

    ![Função](/Scripts/Automocao%20AWS/imgs/funcao-EC2.png)

- Instância criada:

    ![Instância gerada](/Scripts/Automocao%20AWS/imgs/instancia-EC2.png)

- Detalhes da instância:

    ![Detalhes da Instância 1/2](/Scripts/Automocao%20AWS/imgs/detalhes-1-EC2.png)

    ![Detalhes da Instância 2/2](/Scripts/Automocao%20AWS/imgs/detalhes-2-EC2.png)