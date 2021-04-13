from pathlib import Path
import os

from PIL import Image
import numpy as np
import requests
from io import BytesIO
from questions.models import ChineseQuestion, EnglishQuestion
from time import sleep
import random
# from paddleocr import PaddleOCR



from io import BytesIO
from cnocr import CnOcr

ocr = CnOcr(name='img-ocr', model_name='densenet-lite-gru')


# BASE_DIR = Path(__file__).resolve().parent.parent
#
# det_model_dir = os.path.join(BASE_DIR, 'inference/ch_ppocr_server_v2.0_det_infer/')
# rec_model_dir = os.path.join(BASE_DIR, 'inference/ch_ppocr_server_v2.0_rec_infer/')

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

# 服务端
# ocr = PaddleOCR(det_model_dir=det_model_dir, rec_model_dir=rec_model_dir, use_space_char=True)
# ocr = PaddleOCR(use_angle_cls=False, use_space_char=True)

"""
语文图片转换文字脚本
"""
def stepTranTextChinese():
    QModel = ChineseQuestion
    limit = 10

    for i in range(3):
        stepTranTextCommon(QModel, limit)
        sleep(1)


"""
语文图片转换文字脚本
"""
def stepTranTextEnglish():
    QModel = EnglishQuestion
    limit = 10

    for i in range(5):
        stepTranTextCommon(QModel, limit)
        sleep(1)



def stepTranTextCommon(QModel, limit):
    count = QModel.objects.filter(step=1).count()

    skip = 0

    if count > limit:
        skip = random.randint(1, count)


    list = QModel.objects.filter(step=1).order_by('id')[skip:skip+limit]

    if len(list) == 0:
        return

    for item in list:
        try:
            sleep(1)
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
        # res = ocr.ocr(picUrl, cls=False)
        response = requests.get(picUrl)
        img_fp = Image.open(BytesIO(response.content))
        np_image = np.array(img_fp)
        res = ocr.ocr(np_image)
        text = '\n'.join([''.join(a) for a in res])

        return text
    except:
        raise

