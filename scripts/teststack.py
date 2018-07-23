import boto3
client = boto3.client('cloudformation',)
stack= client.describe_stacks(StackName='test111222')
print( "DNS : " + stack['Stacks'][0]['Outputs'][0].get('OutputValue'))
