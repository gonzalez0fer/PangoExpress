# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='asd',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
