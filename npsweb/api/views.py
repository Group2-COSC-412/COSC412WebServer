from django.shortcuts import render
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
import time
import random

# Create your views here.


@login_required(login_url="/home/login")
def es(request: HttpRequest):
    """
    GET params:
        index: "comment", "review", "park", or "picture"
        parkid: currently only the numbers 1-10, maps to a specific park
        tmin: minimum unix epoch time to search by, default is 0
        tmax: maximum unix epoch time to search by, default is current time
        size: number of items to return

    POST params:
        index: "comment", "reviews", "park", or "picture"
        parkid: currently only the numbers 1-10, maps to a specific park

        if parkid is "comment":
            pictureid: numeric id of the picture the comment is mapped to
            comment: full comment as a string

        else if parkid is "review":
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
    if request.method == "GET":
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

        esresponse = {}
        if request.GET.get("index") != 'comment':
            query = {"size": int(request.GET.get("size", 10)),
                     "query": {"bool": {
                                "must": [
                                    {"range": {
                                        "time": {
                                            "gte": request.GET.get("tmin", 0),
                                            "lte": request.GET.get("tmax", time.time()),
                                        }
                                    }},
                                    {"term": {
                                        "parkid": int(request.GET.get("parkid")),
                                    }}
                                ]
                            }}
                     }
            esresponse = esnode.search(index=request.GET.get("index"), body=str(query).replace('\'', '\"'))
        elif request.GET.get("index") == 'comment':
            query = {"size": int(request.GET.get("size", 10)),
                     "query": {"bool": {
                                "must": [
                                    {"range": {
                                        "time": {
                                            "gte": request.GET.get("tmin", 0),
                                            "lte": request.GET.get("tmax", time.time()),
                                        }
                                    }},
                                    {"term": {
                                        "picture_id": int(request.GET.get("pictureid")),
                                    }}
                                ]
                            }}
                     }
            esresponse = esnode.search(index=request.GET.get("index"), body=str(query).replace('\'', '\"'))
        else:
            return HttpResponseBadRequest()

        responsearr = []
        i = 0
        for hit in esresponse['hits']['hits']:
            responsearr.append(hit['_source'])
            i += 1

        return JsonResponse({'hits': responsearr})

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

        allowed_indeces = ['review', 'comment', 'picture']
        index = request.POST.get("index")
        if index in allowed_indeces:
            body = {}
            if index == 'review' and\
                    request.POST.get("parkid") and\
                    request.POST.get("rating") and\
                    request.POST.get("review"):
                body = {
                    'parkid': request.POST.get("parkid"),
                    'rating': request.POST.get("rating"),
                    'review': request.POST.get("review"),
                    'time': time.time(),
                    'user': request.user.get_username()
                }
            elif index == 'comment' and\
                    request.POST.get("pictureid") and\
                    request.POST.get("comment"):
                body = {
                    'picture_id': request.POST.get("pictureid"),
                    'comment': request.POST.get("comment"),
                    'time': time.time(),
                    'user': request.user.get_username()
                }
            elif index == 'picture' and\
                    request.POST.get("parkid") and\
                    request.POST.get("pictureurl"):
                pictureid = generatepicid(esnode)
                body = {
                    'parkid': request.POST.get("parkid"),
                    'picture_url': request.POST.get("pictureurl"),
                    'picture_id': pictureid,
                    'time': time.time(),
                    'user': request.user.get_username()
                }

            esnode.index(index=request.POST.get("index"),
                         doc_type=request.POST.get("index"),
                         body=str(body).replace('\'', '\"'))
            return JsonResponse(body)


def generatepicid(esnode: Elasticsearch):
    rand = random.Random()

    esid = rand.random()
    while esnode.search(index='picture', doc_type='picture', body={
        'query': {
            "term": {
                "picture_id": esid
            }
        }
    })['hits']['total'] > 0:
        esid = rand.random()

    return esid
