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

ocr = CnOcr(name='img-tarn', model_name='densenet-lite-gru')

"""
example
"""
response = requests.get('https://image.jiandan100.cn/images/cqaimages/42/255/2817944_q.jpg')
img_fp = Image.open(BytesIO(response.content))
# img = mx.image.imread(img_fp, 1).asnumpy()

np_image = np.array(img_fp)
res = ocr.ocr(np_image)

text = '\n'.join([''.join(a) for a in res])
print("Predicted Chars:", text)
