from django.shortcuts import render

# Create your views here.
from datetime import date
from .search_indexes import ChineseQuestionIndex
from haystack.generic_views import SearchView
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render

from elasticsearch import Elasticsearch, RequestsHttpConnection


http_auth = ('elastic', 'changeme')

def eSearch(request):
    es_client = Elasticsearch(hosts=['http://localhost'],
                              http_auth=http_auth,
                              port=9200)
    keyword = request.GET['q']

    body = {
        "query": {
            "match": {
                "text": {
                    "query": keyword,
                    "fuzziness": "AUTO",
                    "operator": "and"
                }
            }
        }
    }

    result = es_client.search(index='questions', size=20, doc_type='modelresult', body=body)

    return JsonResponse(result, content_type='application/json', safe=False)

class IndexView(View):

    def get(self, request):
        return render(request, 'search/search.html')

