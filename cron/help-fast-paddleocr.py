from pathlib import Path
import os
from PIL import Image
import numpy as np
import requests
from io import BytesIO
from paddleocr import PaddleOCR, draw_ocr
import cv2

BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)

rec_model_dir = os.path.join(BASE_DIR, 'inference/en_number_mobile_v2.0_rec_infer/')


"""
example
"""

# 模型路径下必须含有model和params文件
ocr = PaddleOCR(rec_model_dir=rec_model_dir, lang='en')
# ocr = PaddleOCR(use_space_char=True)
#det_model_dir='{your_det_model_dir}', rec_model_dir='{your_rec_model_dir}', rec_char_dict_path='{your_rec_char_dict_path}', cls_model_dir='{your_cls_model_dir}', use_angle_cls=True
# img_path = 'https://image.jiandan100.cn/images/cqaimages/42/255/2817944_q.jpg'
# img_path = 'https://image.jiandan100.cn/images/cqaimages/3/73/215296_q.jpg'


response = requests.get('http://8.210.115.9/img.php?num=NjMyMzgy&x=MzM5NDgwNTgzNTk=&s=77600120640')
img_fp = Image.open(BytesIO(response.content))
# img_fp = Image.open('img.png')
np_image = np.array(img_fp)

gray = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)

# print(gray)

t,rst=cv2.threshold(gray, 168,255,cv2.THRESH_BINARY_INV)

result = ocr.ocr(rst, det=False, rec=True, cls=False)

print(result[0][0])
print(result)

# for line in result:
#     print(line)
#     print(line[1][0])

# text = '\n'.join([a[1][0] for a in result])

# print(text)
