from PIL import Image
import numpy as np
import requests
from io import BytesIO
from cnocr import CnOcr
# from questions.models import ChineseQuestion, EnglishQuestion
from time import sleep
import random
import easyocr
import cv2

# ocr = CnOcr(name='img-tarn')

"""
example
"""
reader = easyocr.Reader(['ch_sim','en'])

result = reader.readtext('https://image.jiandan100.cn/images/cqaimages/42/255/2817944_q.jpg', detail = 0)
# result = reader.readtext('http://8.210.115.9/img.php?num=NjMyMzgy', detail = 0)
# result = reader.readtext('https://image.jiandan100.cn/images/cqaimages/4/136/297196_q.jpg', detail = 0)
print(result)

# response = requests.get('https://image.jiandan100.cn/images/cqaimages/4/136/297196_q.jpg')
# img_fp = Image.open(BytesIO(response.content))
# image = cv2.imread('297196_q.jpg')
# print(image)

# np_image = np.array(img_fp)
# res = ocr.ocr(np_image)

text = '\n'.join(result)
print("Predicted Chars:", text)

# result = reader.detect(image)
# print(result)

