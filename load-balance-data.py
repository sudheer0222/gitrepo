#ELB Load Balancer script to fetch the data


import boto3
client = boto3.client('elb')
balancer = client.describe_load_balancers()
print("LoadBalancerName                ","|","DNSName                                                               ","|","CanonicalHostedZoneName")
for i in balancer['LoadBalancerDescriptions']:
    print(i['LoadBalancerName'],"|",i['DNSName'],"|",i['CanonicalHostedZoneName'])
