## TODO

[x] 科目questions 表  
[x] 导入信息
   - 英语
   - 数学
   - 线上全量数据

[x] elk 搜索   
[] 计划任务  


### env

Python 3.7.9
Django 3.1.6


## feature

1. [ocr](https://github.com/breezedeus/cnocr)
2. [easyOcr](https://github.com/JaidedAI/EasyOCR)
3. [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
4. [haystack](http://haystacksearch.org/)
    - 数据导入与搜索


### 导入数据
subjectId 对应

```js
/**
 * 学科编号 同
 * https://jdapi.jd100.com/coursemgr/v1/getSubjectList
 */
export const SUBJECT_NO = {
  CHINESE: 1,  // 语文
  MATHEMATICS: 2, // 数学
  ENGLISH: 3, // 英语
  PHYSICS: 4, // 物理
  CHEMISTRY: 5, // 化学
  BIOLOGY: 6, // 生物
  HISTORY: 7, // 历史
  GEOGRAPHY: 8, // 地理
  POLITICS: 9, // 政治
};

/**
 * 中学学科对应的编号
 */
export const SUBJECT_CHINESE_MAPPER = {
  '语文': 1, // 语文
  '数学': 2, // 数学
  '英语': 3, // 英语
  '物理': 4, // 物理
  '化学': 5, // 化学
  '生物': 6, // 生物
  '历史': 7, // 历史
  '地理': 8, // 地理
  '政治': 9, // 政治
};
```


### script

```shell
# 创建超级管理员
python manage.py createsuperuser


python manage.py crontab add


python manage.py 
```

### 初始化

```shell
# 搭建mysql 和 elk

# 使用 conda 创建环境
conda create -n qs python=3.7

# 安装依赖
pip install -r requirements.txt

# 初始化 环境变量
cp config.template.ini config.ini

# settings 中 配置 elk 地址 
HAYSTACK_CONNECTIONS

# 创建执行迁移文件
python manage.py makemigrations

# 执行迁移文件 （初始化已存在的表）
python manage.py migrate

# 创建超级管理员
python manage.py createsuperuser

# 启动服务 
python manage.py runserver

# 导入SQL数据 dep_server/initsql/query_result.csv

# 执行迁移脚本

# 导入 搜索引擎
python manage.py rebuild_index

# 后台地址
open 'http://127.0.0.1:8000/admin/'

# 题目搜索
open 'http://127.0.0.1:8000/questions/index'
```

### 设计表结构



### 加入搜索

http://haystacksearch.org/

```shell
# 模糊匹配
GET questions/_search
{
  "query": {
    "match": {
      "text": {
        "query":   "情、爱情的期待和渴 大篮子，里面的鸥和鸭子把头伸在篮子外面。我犹豫了好一会儿之后，决定走进车厢。我说，很对不起了，让我来把篮子移开。可是一位穿着工作服的农民对我又说我在登上车",
        "fuzziness": "AUTO",
        "operator":  "and"
      }
    }
  }
}
```


###  安装 paddleocr


```shell
mkdir inference && cd inference

wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_server_v2.0_det_infer.tar && tar xf ch_ppocr_server_v2.0_det_infer.tar
# 下载超轻量级中文OCR模型的识别模型并解压
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_server_v2.0_rec_infer.tar && tar xf ch_ppocr_server_v2.0_rec_infer.tar
# 下载超轻量级中文OCR模型的文本方向分类器模型并解压
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar && tar xf ch_ppocr_mobile_v2.0_cls_infer.tar
cd ..
```