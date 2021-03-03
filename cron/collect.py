
import os
import sys
import random
import django
from datetime import date

from django.db.models import Max, Min, Q
from questions.models import ChineseQuestion
from origin.models import SectionInfo

os.environ['DJANGO_SETTINGS_MODULE'] = 'question_ocr_search.settings'  # 设置项目的配置文件


maxLen = 10

def importChinese():
    res = ChineseQuestion.objects.aggregate(max_id=Max('origin_id'))
    maxId = res.get('max_id')
    nextId = maxId if maxId else 0
    list = SectionInfo.objects.filter(~Q(sectiontitle=''), subjectid=1, id_inc__gt=nextId).order_by('id_inc')[:maxLen]

    for item in list:
        question = ChineseQuestion()
        question.pic_title = f"https://image.jiandan100.cn/images/cqaimages/{item.sectiontitle}"
        question.pic_answer = f"https://image.jiandan100.cn/images/cqaimages/{item.sectionkey}"
        question.origin_id = item.id_inc
        question.save()

