# Generated by Django 3.1.6 on 2021-03-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210304_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='chinesequestion',
            name='same_guids',
            field=models.TextField(default='', verbose_name='同类题guid'),
        ),
        migrations.AddField(
            model_name='englishquestion',
            name='same_guids',
            field=models.TextField(default='', verbose_name='同类题guid'),
        ),
    ]
