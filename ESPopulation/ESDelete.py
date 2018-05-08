from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

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
    if input("Are you sure you wish to delete everything from the database? [y/N]") == "Y":
        if input("Are you really sure??? [y/N]") == "Y":
            if input("Are sure that you're sure?? [y/N]") == "Y":
                esnode.indices.delete("reviews")
                esnode.indices.delete("comment")
                esnode.indices.delete("park")
                esnode.indices.delete("picture")
