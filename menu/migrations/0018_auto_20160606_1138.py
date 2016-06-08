# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 11:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_auto_20160604_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fechaNacimiento',
            field=models.DateField(default=datetime.datetime(2016, 6, 6, 11, 38, 33, 370670, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
