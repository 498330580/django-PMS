# Generated by Django 2.2.7 on 2020-01-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_pms', '0005_auto_20200108_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='path',
            field=models.CharField(default='welcome', help_text='前端要访问的菜单路径', max_length=50, verbose_name='菜单路径地址'),
        ),
    ]
