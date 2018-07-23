import boto3
import sys
import requests

client = boto3.client('cloudformation',)
stack= client.describe_stacks(StackName='test111222')
print( "DNS : " + stack['Stacks'][0]['Outputs'][0].get('OutputValue'))

loadbalancerDnsName = stack['Stacks'][0]['Outputs'][0].get('OutputValue')
if not loadbalancerDnsName :
    print("Error getting LoadBalancer Dns")
    sys.exit()
    
r = requests.get(loadbalancerDnsName)
if r.status_code == 200:
    print("WEbsite reachable")
else:
    print("website not reachable")
    



