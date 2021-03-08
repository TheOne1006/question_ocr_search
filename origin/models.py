from django.db import models


# export const SUBJECT_NO = {
#   CHINESE: 1,  // 语文
#   MATHEMATICS: 2, // 数学
#   ENGLISH: 3, // 英语
#   PHYSICS: 4, // 物理
#   CHEMISTRY: 5, // 化学
#   BIOLOGY: 6, // 生物
#   HISTORY: 7, // 历史
#   GEOGRAPHY: 8, // 地理
#   POLITICS: 9, // 政治
# };



# Create your models here.
class SectionInfo(models.Model):
    """例题"""
    id_inc = models.AutoField(primary_key=True)
    sectiontitle = models.TextField(default="", verbose_name="题目图片")
    sectionkey = models.TextField(default="", verbose_name="答案图片")
    subjectid = models.IntegerField(choices=((1, "语文"), (2, "数学"), (3, "英语"), (4, "物理")), default="0", verbose_name="学科id")
    samesectiondata = models.TextField(default="", verbose_name="同类题id")

    class Meta:
        managed = False
        db_table = 'W_SectionInfo'


    def __str__(self):
        return self.sectiontitle


class SameSectionInfo(models.Model):
    """同类题"""
    id = models.AutoField(primary_key=True)
    guid = models.TextField(default="", verbose_name="guid")
    sectiontitle = models.TextField(default="", verbose_name="题目图片")
    sectionanswer = models.TextField(default="", verbose_name="答案图片")

    class Meta:
        managed = False
        db_table = 'W_SameSectionInfo'

    def __str__(self):
        return self.sectiontitle


