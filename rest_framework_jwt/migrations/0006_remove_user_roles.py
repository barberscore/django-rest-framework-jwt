# Generated by Django 2.2.3 on 2019-07-27 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_jwt', '0005_auto_20190726_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
    ]