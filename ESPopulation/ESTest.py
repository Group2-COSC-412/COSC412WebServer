from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import time

if __name__ == "__main__":
    keys = open("/home/ubuntu/keys/Django-User-AWS.key", 'r')
    aws_key = keys.readline().replace('\n', '')
    aws_secret = keys.readline().replace('\n', '')
    endpoint = keys.readline().replace('\n', '')
    keys.close()

    region = "us-east-1"
    service = "es"
    aws_auth = AWS4Auth(aws_key, aws_secret, region, service)
    esnode = Elasticsearch(
        hosts=[{'host': endpoint, 'port': 443}],
        http_auth=aws_auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    query = {"size": 100,
             "query": {
                 "bool": {
                     "must": [
                         {"range": {
                             "time": {
                                 "gte": 0,
                                 "lte": str(time.time())
                             }
                         }},
                         {"term": {
                             "parkid": 1
                         }}
                     ]
                 }
             }
    }

    print(esnode.search(index=None, body=str(query).replace('\'', '\"')))