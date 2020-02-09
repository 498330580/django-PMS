# Generated by Django 3.0.2 on 2020-02-07 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='设置网站的名称', max_length=30, verbose_name='网站名称')),
                ('logo', models.ImageField(default='WebsiteConfig/logo.png', max_length=250, upload_to='WebsiteConfig/%Y/%m/%d/', verbose_name='网站LOGO')),
            ],
            options={
                'verbose_name': '前端网站设置',
                'verbose_name_plural': '前端网站设置',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='菜单名称', max_length=30, verbose_name='菜单名称')),
                ('path', models.CharField(default='welcome', help_text='前端要访问的菜单路径', max_length=50, verbose_name='菜单路径地址')),
                ('desc', models.TextField(default='', help_text='菜单描述', verbose_name='菜单描述')),
                ('index', models.IntegerField(default=999, verbose_name='菜单顺序')),
                ('category_type', models.IntegerField(choices=[(1, '一级菜单'), (2, '二级菜单'), (3, '三级菜单')], help_text='类目级别', verbose_name='类目级别')),
                ('class_img', models.CharField(default='', help_text='Element图标', max_length=100, verbose_name='class图标')),
                ('is_look', models.BooleanField(default=False, help_text='是否显示到菜单中', verbose_name='是否显示')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父菜单', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='vue_pms.Menu', verbose_name='父类菜单级别')),
            ],
            options={
                'verbose_name': '菜单设置',
                'verbose_name_plural': '菜单设置',
                'ordering': ['index'],
            },
        ),
    ]
