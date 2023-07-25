from config import DBSession
from hashids import Hashids
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr

hashids = Hashids(salt="BBRRICKKK")

def log_shorturl(url):
    original_url=url
    id=hashids.encode(int(datetime.now().timestamp()*1000))
    DBSession.put_item(
        Item={
            'id': id,
            'url': original_url,
            'created_at': datetime.now().isoformat("T")
        }
    )
    return id

def retrieve_url(id):
    print(id)
    fe=Key('id').eq(id)
    results = DBSession.scan(FilterExpression=fe)
    while 'LastEvaluatedKey' in results and not results['Items']:
        results = DBSession.scan(ExclusiveStartKey=results['LastEvaluatedKey'],FilterExpression=fe)

    if not results['Items']:
        return None
    else:
        return results['Items'][0]['url']

