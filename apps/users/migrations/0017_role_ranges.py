# Generated by Django 3.0.2 on 2020-01-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0003_daduizhongduitype'),
        ('users', '0016_personalinformation_fenzu'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='ranges',
            field=models.ManyToManyField(blank=True, help_text='角色控制数据的权限范围', to='classification.DaduiZhongduiType', verbose_name='权限范围'),
        ),
    ]