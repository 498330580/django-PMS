# Generated by Django 3.0.2 on 2020-01-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='birthday',
            field=models.DateField(blank=True, help_text='系统会根据身份证自动填写', verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='男', help_text='默认为“男”,系统会根据身份证自动判断', max_length=5, verbose_name='性别'),
        ),
    ]
