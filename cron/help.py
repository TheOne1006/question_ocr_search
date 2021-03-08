
import os
import sys
import random
import django
from datetime import date

from django.db.models import Max, Min, Q
from questions.models import ChineseQuestion
from origin.models import SectionInfo
from time import sleep
import requests

os.environ['DJANGO_SETTINGS_MODULE'] = 'question_ocr_search.settings'  # 设置项目的配置文件



def replenish():
    list = ChineseQuestion.objects.filter(same_guids='', origin_type='section')

    for item in list:
        sectionInfo = SectionInfo.objects.get(id_inc=item.origin_id)

        if sectionInfo.samesectiondata:
            try:
                item.same_guids = sectionInfo.samesectiondata
                item.save()
            except:
                print(item.id)
