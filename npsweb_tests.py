from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import time
import random


def es_get_test(esnode):
    query = {"size": 100,
             "query": {"bool": {
                 "must": [
                     {"range": {
                         "time": {
                             "gte": 0,
                             "lte": time.time(),
                         }
                     }},
                     {"term": {
                         "parkid": 1,
                     }}
                 ]
             }}
             }
    for index in ['review', 'park', 'picture']:
        esresponse = esnode.search(index=index, body=str(query).replace('\'', '\"'))
        print(esresponse)
        print('\n\n')

    query = {"size": 100,
             "query": {"bool": {
                 "must": [
                     {"range": {
                         "time": {
                             "gte": 0,
                             "lte": time.time(),
                         }
                     }},
                     {"term": {
                         "picture_id": 1,
                     }}
                 ]
             }}
             }
    esresponse = esnode.search(index="comment", body=str(query).replace('\'', '\"'))
    print(esresponse)


def es_post_test(esnode):
    pass


def main():
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
    es_get_test(esnode)




if __name__ == "__main__":
    main()