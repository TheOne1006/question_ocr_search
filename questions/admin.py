from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.
from .models import ChineseQuestion, EnglishQuestion

class QuestionAdmin(admin.ModelAdmin):
    # 方法一
    def titlepic(self, obj):  # imageField显示方法设置,图片路径设为显示图片
        return mark_safe('<img src="%s" max-height="220" max-width="220" />' % obj.pic_title)

    # 方法二
    def answerpic(self, obj):
        return mark_safe('<img src="%s" max-height="220" max-width="220" />' % obj.pic_answer)

    # 显示页面显示字段设置,只有改变标记标记方法时,加入的字段才不加引号
    list_display = ( 'id', 'titlepic', 'answerpic',)

    search_fields = ('titlepic',)

    # list_filter = ('subjectid',)

    readonly_fields = ('titlepic', 'answerpic',)

admin.site.register(ChineseQuestion, QuestionAdmin)
admin.site.register(EnglishQuestion, QuestionAdmin)
