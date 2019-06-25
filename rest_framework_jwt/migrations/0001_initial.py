# Generated by Django 2.1.9 on 2019-06-24 21:33

from django.db import migrations, models
import rest_framework_jwt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', rest_framework_jwt.fields.LowerEmailField(blank=True, help_text='\n            The contact email of the resource.', max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'rest_framework_jwt_user',
            },
        ),
    ]
