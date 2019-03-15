# Load Balancer details
import boto3
client = boto3.client('elb')
balancer = client.describe_load_balancers()
columns_format="%-35s %-70s %-50s"
print(columns_format%("LoadBalancerName","DNSName","CanonicalHostedZoneName"))
for i in range(len(balancer.get('LoadBalancerDescriptions'))):
    print(columns_format %(
                           balancer.get('LoadBalancerDescriptions')[i].get('LoadBalancerName'),
                           balancer.get('LoadBalancerDescriptions')[i].get('DNSName'),
                           balancer.get('LoadBalancerDescriptions')[i].get('CanonicalHostedZoneName')
                           ))
