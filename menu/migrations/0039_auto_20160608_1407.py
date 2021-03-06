# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0038_auto_20160608_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='pseudonimo',
            field=models.CharField(max_length=100, unique=True, validators=[menu.models.validate_pseudonimo]),
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
    ]
