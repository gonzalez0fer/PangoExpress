# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0063_auto_20160609_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=11, validators=[menu.models.validate_telefono]),
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
    ]
