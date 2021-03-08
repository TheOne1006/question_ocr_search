from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.

from .models import SectionInfo, SameSectionInfo


class SectionAdmin(admin.ModelAdmin):
    # 方法一
    def titlepic(self, obj):  # imageField显示方法设置,图片路径设为显示图片
        if obj.sectiontitle:
            return mark_safe('<img src="https://image.jiandan100.cn/images/cqaimages/%s" height="220" />' % obj.sectiontitle)

        return ''

    # 方法二
    def answerpic(self, obj):
        # 返回方法1
        # return format_html('<img src="{}" height="20" />', format(obj.公司logo.url))
        # 返回方法2
        return format_html('<img src="https://image.jiandan100.cn/images/cqaimages/%s" height="220" />' % obj.sectionkey)

    # 显示页面显示字段设置,只有改变标记标记方法时,加入的字段才不加引号
    list_display = ( 'subjectid', 'sectiontitle', 'titlepic',)

    search_fields = ('sectiontitle',)

    list_filter = ('subjectid',)

    readonly_fields = ('titlepic', 'answerpic',)


class SameAdmin(admin.ModelAdmin):

    # 方法一
    def titlepic(self, obj):  # imageField显示方法设置,图片路径设为显示图片
        if obj.sectiontitle :
            return mark_safe('<img src="https://image.jiandan100.cn/images/cqaimages/%s" height="220" />' % obj.sectiontitle)

        return ''

    # 方法二
    def answerpic(self, obj):
        # 返回方法1
        # return format_html('<img src="{}" height="20" />', format(obj.公司logo.url))
        # 返回方法2
        return format_html('<img src="https://image.jiandan100.cn/images/cqaimages/%s" height="220" />' % obj.sectionkey)

    # 显示页面显示字段设置,只有改变标记标记方法时,加入的字段才不加引号
    list_display = ('sectiontitle', 'titlepic',)

    search_fields = ('sectiontitle',)

    readonly_fields = ('titlepic', 'answerpic',)


admin.site.register(SectionInfo, SectionAdmin)

admin.site.register(SameSectionInfo, SameAdmin)

