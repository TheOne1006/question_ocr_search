# search_indexes.py   # search_indexes名字不能改，固定

from haystack import indexes
from .models import ChineseQuestion

class ChineseQuestionIndex(indexes.SearchIndex, indexes.Indexable):
    """
    ChineseQuestion 索引类
    """
    # text表示被查询的字段，用户搜索的是这些字段的值，具体被索引的字段写在另一个文件里。
    text = indexes.CharField(document=True, use_template=True)

    # 保存在索引库中的字段
    pic_title = indexes.CharField(model_attr='pic_title')
    pic_answer = indexes.CharField(model_attr='pic_answer')

    qid = indexes.IntegerField(model_attr='id')
    origin_id = indexes.IntegerField(model_attr='origin_id')
    origin_type = indexes.CharField(model_attr='origin_type')
    model_version = indexes.IntegerField(model_attr='version')

    def get_model(self):
        """返回建立索引的模型类"""
        return ChineseQuestion

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_deleted=False)