from PIL import Image
import numpy as np
import requests
from io import BytesIO
from cnocr import CnOcr
# from questions.models import ChineseQuestion, EnglishQuestion
from time import sleep
import random
from cnocr.line_split import line_split
import mxnet as mx
import cv2

ocr = CnOcr(name='img-tarn', model_name='densenet-lite-gru')

"""
example
"""
# response = requests.get('https://image.jiandan100.cn/images/cqaimages/42/255/2817944_q.jpg')
response = requests.get('http://8.210.115.9/img.php?num=NjMyMzgy&x=MzM5NDgwNTgzNTk=&s=77600120640')
img_fp = Image.open(BytesIO(response.content))
# img_fp = Image.open('img.png')
np_image = np.array(img_fp)

gray = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)

# print(gray)

t,rst=cv2.threshold(gray, 168,255,cv2.THRESH_BINARY_INV)

# cv2.imshow('t', gray)
# cv2.imshow('rst', rst)

# cv2.waitKey(0)
# img = mx.image.imread(img_fp, 1).asnumpy()


res = ocr.ocr(rst)

text = '\n'.join([''.join(a) for a in res])
print("Predicted Chars:", text)
