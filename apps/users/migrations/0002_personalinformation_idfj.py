# Generated by Django 3.0.2 on 2020-02-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='idfj',
            field=models.CharField(default='', help_text='辅警编号', max_length=10, verbose_name='辅警编号'),
        ),
    ]
