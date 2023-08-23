# Generated by Django 3.2.4 on 2023-08-11 09:56

import Codeproject.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, max_length=16, null=True, unique=True)),
            ],
            options={
                'db_table': 'user_master',
            },
            managers=[
                ('objects', Codeproject.manager.CustomUserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='usermaster',
            index=models.Index(fields=['email', 'mobile_number', 'id'], name='user_master_email_03bf9f_idx'),
        ),
    ]
