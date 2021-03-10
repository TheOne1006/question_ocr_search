from pathlib import Path
import os
from PIL import Image
import numpy as np
import requests
from io import BytesIO
from paddleocr import PaddleOCR, draw_ocr


BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)

det_model_dir = os.path.join(BASE_DIR, 'inference/ch_ppocr_server_v2.0_det_infer/')
rec_model_dir = os.path.join(BASE_DIR, 'inference/ch_ppocr_server_v2.0_rec_infer/')
cls_model_dir = os.path.join(BASE_DIR, 'inference/ch_ppocr_mobile_v2.0_cls_infer/')

"""
example
"""



# 模型路径下必须含有model和params文件
ocr = PaddleOCR(det_model_dir=det_model_dir, rec_model_dir=rec_model_dir, use_space_char=True)
# ocr = PaddleOCR(use_space_char=True)
#det_model_dir='{your_det_model_dir}', rec_model_dir='{your_rec_model_dir}', rec_char_dict_path='{your_rec_char_dict_path}', cls_model_dir='{your_cls_model_dir}', use_angle_cls=True
# img_path = 'https://image.jiandan100.cn/images/cqaimages/42/255/2817944_q.jpg'
img_path = 'https://image.jiandan100.cn/images/cqaimages/3/73/215296_q.jpg'
result = ocr.ocr(img_path)

for line in result:
    print(line)
    print(line[1][0])

text = '\n'.join([a[1][0] for a in result])

print(text)
