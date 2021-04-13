
import os
import sys
import random
import django
from datetime import date

from django.db.models import Max, Min, Q
from questions.models import ChineseQuestion, EnglishQuestion
from origin.models import SectionInfo, SameSectionInfo
from time import sleep
import requests

os.environ['DJANGO_SETTINGS_MODULE'] = 'question_ocr_search.settings'  # 设置项目的配置文件


def importEnglish():
    """
    核心题库
    导入英语信息
    """
    subject = 3
    QModel = EnglishQuestion
    limit = 1000

    preNextId = 30800

    for i in range(100):
        preNextId = importCoreSection(subject, QModel, limit, preNextId)
        print(preNextId)
        sleep(1)

    for i in range(1000):
        importSameSection(QModel, limit)




def importChinese():
    """
    核心题库
    导入语文信息
    """
    subject = 1
    QModel = ChineseQuestion
    limit = 1000

    preNextId = 30800

    for i in range(10):
        preNextId = importCoreSection(subject, QModel, limit, preNextId)
        print(preNextId)
        sleep(1)

    for i in range(10):
        importSameSection(QModel, limit)



def importSameSection(QModel, limit):
    res = QModel.objects.filter(~Q(same_guids=''), origin_type='section').order_by('id').first()
    maxId = res.id
    nextId = maxId if maxId else 0

    print(nextId)

    list = QModel.objects.filter(~Q(same_guids=''), origin_type='section', id__gt=nextId).order_by('id')[:limit]

    print(len(list))

    if len(list) == 0:
        return

    for item in list:
        arr = item.same_guids.split(',')
        for arrItem in arr:
            instance = SameSectionInfo.objects.get(guid=arrItem)

            if not instance:
                continue

            if instance.sectiontitle and instance.sectionanswer:
                titleurl = f"https://image.jiandan100.cn/images/cqaimages/{instance.sectiontitle}"
                answerurl = f"https://image.jiandan100.cn/images/cqaimages/{instance.sectionanswer}"

                importQuestionItem('same', titleurl, answerurl, instance.id, '', QModel)



def importQuestionItem(origin_type, titleurl, answerurl, origin_id, same_guids, QModel):
    """
    导入题目
    """

    # 去掉重复数据
    instance = QModel.objects.filter(pic_title=titleurl).first()

    # print(instance)

    if instance:
        return

    # 尝试获取
    response = requests.get(titleurl)

    if (response.status_code != 200):
        return

    responseAnswer = requests.get(answerurl)

    if (responseAnswer.status_code != 200):
        return

    question = QModel()
    question.origin_type = origin_type
    question.pic_title = titleurl
    question.pic_answer = answerurl
    question.origin_id = origin_id
    question.same_guids = same_guids

    question.save()



def importCoreSection(subject, QModel, limit, preNextId):
    """
    导入数据，过滤无法访问的图片,过滤重复数据
    返回最后一条 origin id
    """
    res = QModel.objects.filter(origin_type='section').order_by('origin_id').first()

    maxId = 0
    if res:
        maxId = res.origin_id

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

        importQuestionItem('section', titleurl, answerurl, item.id_inc, item.samesectiondata, QModel)

    return list[len(list) - 1].id_inc