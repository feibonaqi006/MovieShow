import redis
from django.shortcuts import render
from elasticsearch import Elasticsearch
from .items import Movie

client = Elasticsearch(hosts=["127.0.0.1"])
redis_cli = redis.StrictRedis()


def hello(request):
    key = '中国大陆'
    response = client.search(
        index="moviedata",
        body={
            "query": {
                "match": {
                    "movie_country": key
                }
            }
        }
    )
    hit_list = []
    for hit in response["hits"]["hits"]:
        hit_list.append(hit['_source'])
        print(hit)

    return render(request, 'index.html', {"data": hit_list})
