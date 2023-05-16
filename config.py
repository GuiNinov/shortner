# load and connect SSM
import boto3


ssm = boto3.client('ssm', 'us-east-2')

dynamodb = boto3.resource('dynamodb',"us-east-2")
#table name
DBSession = dynamodb.Table('shortener')


# Get value Function
def get_parameters(name):
    response = ssm.get_parameter(
        Name=name
    )
    return response['Parameter']['Value']


# Get External Service Parameters
microservices_key=get_parameters('microsservices-key')

