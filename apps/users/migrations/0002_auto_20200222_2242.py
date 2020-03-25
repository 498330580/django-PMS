# Generated by Django 3.0.2 on 2020-02-22 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='users.PersonalInformation', verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='measureinformation',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lt', to='users.PersonalInformation', verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='physicalexamination',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tj', to='users.PersonalInformation', verbose_name='姓名'),
        ),
    ]
