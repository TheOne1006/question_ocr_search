import os
import sys
import random
import django
from datetime import date

from questions.models import EnglishQuestion

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__).resolve().parent))
sys.path.append(project_path)  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'question_ocr_search.settings'  # 设置项目的配置文件
django.setup()


list2 = EnglishQuestion.objects.all()

print(len(list2))

