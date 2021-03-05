from PIL import Image
import numpy as np
import requests
from io import BytesIO
from cnocr import CnOcr
from questions.models import ChineseQuestion
from time import sleep

ocr = CnOcr()

"""
example
"""
# response = requests.get('https://image.jiandan100.cn/images/cqaimages/42/255/2817942_q.jpg')
# img_fp = Image.open(BytesIO(response.content))
# np_image = np.array(img_fp)
# res = ocr.ocr(np_image)
#
# text = '\n'.join([''.join(a) for a in res])
# print("Predicted Chars:", text)


"""
语文图片转换文字脚本
"""
def stepTranTextChinese():
    QModel = ChineseQuestion
    limit = 10

    for i in range(10):
        stepTranTextCommon(QModel, limit)
        sleep(1)



def stepTranTextCommon(QModel, limit):
    list = QModel.objects.filter(step=1).order_by('id')[:limit]

    if len(list) == 0:
        return

    for item in list:
        try:
            updateInsstance(item, QModel)
        except:
            print(item.id)
            print('tranText Error')





def updateInsstance(instance, QuestionModel):

    try:
        textTitle = tran2text(instance.pic_title)
        textAnswer = tran2text(instance.pic_answer)

        instance.text_answer = textAnswer
        instance.text_title = textTitle

        QuestionModel.objects.filter(id=instance.id, version=instance.version, step=1)\
            .update(text_answer=textAnswer, text_title=textTitle, version=instance.version+1, step=2)
    except:
        raise



def tran2text(picUrl):
    try:
        response = requests.get(picUrl)
        img_fp = Image.open(BytesIO(response.content))
        np_image = np.array(img_fp)
        res = ocr.ocr(np_image)
        text = '\n'.join([''.join(a) for a in res])

        return text
    except:
        raise

