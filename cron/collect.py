
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



def importChinese():
    """
    导入语文信息
    """
    subject = 1
    QModel = ChineseQuestion
    limit = 1000

    preNextId = 922942

    for i in range(100):
        preNextId = importQuestion(subject, QModel, limit, preNextId)
        print(preNextId)
        sleep(1)



def importQuestion(subject, QModel, limit, preNextId):
    """
    导入数据，过滤无法访问的图片,过滤重复数据
    返回最后一条 origin id
    """
    res = ChineseQuestion.objects.aggregate(max_id=Max('origin_id'))
    maxId = res.get('max_id')
    nextId = maxId if maxId else preNextId

    print(preNextId)
    print(maxId)
    print(nextId)

    list = SectionInfo.objects.filter(~Q(sectiontitle='', sectionkey=''), subjectid=subject, id_inc__gt=nextId).order_by('id_inc')[:limit]

    print(len(list))

    if len(list) == 0:
        return

    for item in list:
        titleurl = f"https://image.jiandan100.cn/images/cqaimages/{item.sectiontitle}"
        answerurl = f"https://image.jiandan100.cn/images/cqaimages/{item.sectionkey}"

        # 去掉重复数据
        instance = QModel.objects.filter(pic_title=titleurl).first()

        # print(instance)


        if instance:
            continue

        # 尝试获取
        response = requests.get(titleurl)

        if (response.status_code != 200):
            continue

        responseAnswer = requests.get(answerurl)

        if (responseAnswer.status_code != 200):
            continue

        # print(type(response.status_code))
        # print(response.status_code)

        # sleep(1)
        question = QModel()
        question.pic_title = titleurl
        question.pic_answer = answerurl
        question.origin_id = item.id_inc
        question.save()

    return list[len(list) - 1].id_inc