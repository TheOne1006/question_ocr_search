
import os
import sys
import random
import django
from datetime import date

from questions.models import EnglishQuestion

os.environ['DJANGO_SETTINGS_MODULE'] = 'question_ocr_search.settings'  # 设置项目的配置文件

def demo():
    list2 = EnglishQuestion.objects.all()

    print(len(list2))