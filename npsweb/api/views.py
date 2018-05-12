from django.shortcuts import render
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from django.http import HttpRequest, HttpResponseForbidden, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/auth/login/")
def es(request: HttpRequest):
    if request.method == "GET" and\
            "index" in request.GET and\
            "parkid" in request.GET:
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

        query = {}
        esresponse = esnode.search(index=request.GET.get("index"), body=str(query).replace('\'', '\"'))

        return JsonResponse(esresponse)

    elif request.method == "POST":
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
        return HttpResponse('')
