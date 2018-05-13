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

    for i in range(20):
        review = {"time": time.time(),
                  "rating": (i % 5) + 1,
                  "parkid": i,
                  "review": "I liked this park. This is an example review for park number " + str(i),
                  "user": "cgood"}

        comment = {"time": time.time(),
                   "picture_id": i*i,
                   "user": "cgood",
                   "comment": "Wow! great picture for picture id " + str(i*i)}

        picture = {"time": time.time(),
                   "picture_url": "https://s3.amazonaws.com/cosc-412-s3/ParkImage_" + str(i) + ".jpg",
                   "user": "cgood",
                   "picture_id": i*i,
                   "parkid": i}

        park = {"time": time.time(),
                "parkid": i,
                "location": "123 Fake RD, Not a Town, State 12345",
                "Name": "National Park " + str(i + 1)}
        esnode.index(index="review", doc_type="review", body=str(review).replace('\'', '\"'))
        esnode.index(index="comment", doc_type="comment", body=str(comment).replace('\'', '\"'))
        esnode.index(index="picture", doc_type="picture", body=str(picture).replace('\'', '\"'))
        esnode.index(index="park", doc_type="park", body=str(park).replace('\'', '\"'))
        time.sleep(1)
