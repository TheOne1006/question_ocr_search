from django.contrib import admin

# Register your models here.
from .models import ChineseQuestion, EnglishQuestion

admin.site.register(ChineseQuestion)
admin.site.register(EnglishQuestion)
