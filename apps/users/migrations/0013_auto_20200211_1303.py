# Generated by Django 3.0.2 on 2020-02-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200208_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dangtuan',
            options={'ordering': ['-start', '-create_time'], 'verbose_name': '党团关系', 'verbose_name_plural': '党团关系'},
        ),
        migrations.AddField(
            model_name='dangtuan',
            name='is_effective',
            field=models.BooleanField(default=True, help_text='是否有效', verbose_name='是否有效'),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='users.PersonalInformation', verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='lvli',
            name='name',
            field=models.ForeignKey(help_text='姓名', on_delete=django.db.models.deletion.CASCADE, related_name='lvlis', to='users.PersonalInformation', verbose_name='姓名'),
        ),
    ]
