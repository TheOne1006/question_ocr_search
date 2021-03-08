from django.db import models

# Create your models here.


class commonQuestions(models.Model):
    """通用"""
    id = models.AutoField(primary_key=True)
    pic_title = models.TextField(default="", verbose_name="题目图片")
    pic_answer = models.TextField(default="", verbose_name="答案图片")
    origin_id = models.IntegerField(default="0", verbose_name="原id")
    origin_type = models.CharField(max_length=20, default="section", verbose_name="题目类型")
    step = models.IntegerField(default="1", verbose_name="步骤")
    text_title = models.TextField(default="", verbose_name="题目文本")
    text_answer = models.TextField(default="", verbose_name="答案文本")
    same_guids = models.TextField(default="", verbose_name="同类题guid")
    version = models.IntegerField(default="0", verbose_name="版本")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_deleted = models.BooleanField(default=False, verbose_name="删除")

    class Meta:
        abstract = True

    def __str__(self):  # Python2:__unicode__
        return self.pic_title


class ChineseQuestion(commonQuestions):
    """语文提目表"""

    class Meta:
        verbose_name = "语文题集"
        db_table = "questions_chinese"
        verbose_name_plural = verbose_name


class EnglishQuestion(commonQuestions):
    """英文提目表"""

    class Meta:
        verbose_name = "英文题集"
        db_table = "questions_english"
        verbose_name_plural = verbose_name

