# Generated by Django 3.0.2 on 2020-02-08 00:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200207_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dangtuan',
            options={'ordering': ['-start'], 'verbose_name': '党团关系', 'verbose_name_plural': '党团关系'},
        ),
        migrations.AlterModelOptions(
            name='yonggong',
            options={'ordering': ['-start'], 'verbose_name': '用工信息', 'verbose_name_plural': '用工信息'},
        ),
        migrations.AddField(
            model_name='dangtuan',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dangtuan',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='dangtuan',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
