from datetime import datetime
import boto3

def lambda_handler(event, context):
    # Listando regioes
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    for region in regions:

        print('Instances in EC2 Region {0}:'.format(region)) # Obtém uma lista de nomes de regiões da AWS
        ec2 = boto3.resource('ec2', region_name=region)

        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']} # Filtra instâncias com a tag 'backup' definida como 'true'
            ]
        )

        # Adicionando timestamp
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

        for i in instances.all():
            for v in i.volumes.all():

                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)

                snapshot = v.create_snapshot(Description=desc) # Cria um snapshot do volume atual com a descrição especificada

                print("Created snapshot:", snapshot.id)
