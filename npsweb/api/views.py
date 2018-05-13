from django.shortcuts import render
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from django.http import HttpRequest, HttpResponseForbidden, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/home/login")
def es(request: HttpRequest):
    """
    GET params:
        index: "comment", "reviews", "park", or "picture"
        parkid: currently only the numbers 1-10, maps to a specific park
        tmin: minimum unix epoch time to search by
        tmax: maximum unix epoch time to search by

    POST params:
        index: "comment", "reviews", "park", or "picture"
        parkid: currently only the numbers 1-10, maps to a specific park

        if parkid is "comment":
            pictureid: numeric id of the picture the comment is mapped to
            comment: full comment as a string

        else if parkid is "reviews":
            parkid: id of park the review is for
            review: full review as a string
            rating: 1-5 integer

        else if parkid is "park": # NOTE THAT USER MUST BE AN ADMIN TO POST A PARK
            name: full name of the park
            location: street address of the park

        else if parkid is "picture":
            parkid: id of park to map picture to
            pictureurl: name of the picture file on the S3 bucket

    :param request:
    :return:
    """
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
