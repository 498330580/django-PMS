# Generated by Django 3.0.2 on 2020-01-30 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_role_ranges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='ranges',
            new_name='ranges_fenzu',
        ),
    ]