from django.shortcuts import render

# Create your views here.
from PIL import Image
import numpy as np
from cnocr import CnOcr
from io import BytesIO
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render

from elasticsearch import Elasticsearch

ocr = CnOcr(name='post-image')
http_auth = ('elastic', 'changeme')

def eSearch(request):
    es_client = Elasticsearch(hosts=['http://localhost'],
                              http_auth=http_auth,
                              port=9200)
    keyword = request.GET['q']

    picfile = request.FILES.get('file')

    if (picfile):
        """存在上传图片"""

        img_fp = Image.open(picfile)
        np_image = np.array(img_fp)
        res = ocr.ocr(np_image)
        keyword = '\n'.join([''.join(a) for a in res])


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

