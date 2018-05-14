from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import time
import random


# this is the same query that the GET requests form in api/views.py
def es_get_test(esnode: Elasticsearch):
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


# this is the same query that the POST requests form in api/views.py
def es_post_test(esnode: Elasticsearch):
    allowed_indeces = ['review', 'comment', 'picture']
    parkid = 22222222222222222222222222222222222222
    pictureid = 11111111111111111111111111111111111
    user = 'testuser1@gmail.com'
    for index in allowed_indeces:
        body = {}
        searchbody = {"query": {
                        "term": {
                            "user": user
                        }
                    }}
        if index == 'review':
            body = {
                'parkid': parkid,
                'rating': 5,
                'review': "wow great park!",
                'time': time.time(),
                'user': user
            }
        elif index == 'comment':
            body = {
                'picture_id': pictureid,
                'comment': "wow great picture!",
                'time': time.time(),
                'user': user
            }
        elif index == 'picture':
            body = {
                'parkid': parkid,
                'picture_url': "fake.com",
                'picture_id': pictureid,
                'time': time.time(),
                'user': user
            }

        esnode.index(index=index,
                     doc_type=index,
                     body=str(body).replace('\'', '\"'))
        print(esnode.search(index=index, body=str(searchbody).replace('\'', '\"')))

        esnode.delete_by_query(index=index, body=str(searchbody).replace('\'', '\"'))


# NOTE that this won't work if run locally, because you need AWS access keys
# Please contact Chris if you need to run these yourself, he will give you a temporary key
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