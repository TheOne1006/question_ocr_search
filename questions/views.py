from django.shortcuts import render

# Create your views here.
from datetime import date
from .search_indexes import ChineseQuestionIndex
from haystack.generic_views import SearchView
from django.http import JsonResponse

from elasticsearch import Elasticsearch, RequestsHttpConnection


http_auth = ('elastic', 'changeme')

def eSearch(request):
    es_client = Elasticsearch(hosts=['http://localhost'],
                              http_auth=http_auth,
                              port=9200)
    body = {
        "query": {
            "match": {
                "text": {
                    "query": "我的心中已没有瀑布了。我的心随潭水的绿而摇荡。那醉人的绿呀，仿佛一开两臂",
                    "fuzziness": "AUTO",
                    "operator": "and"
                }
            }
        }
    }

    result = es_client.search(index='questions', size=20, doc_type='modelresult', body=body)

    return JsonResponse(result, content_type='application/json', safe=False)



