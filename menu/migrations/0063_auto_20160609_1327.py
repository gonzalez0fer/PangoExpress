# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0062_auto_20160608_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUENTA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(default=0)),
                ('pagada', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.CLIENTE')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoEnCuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.CUENTA')),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.PLATO')),
            ],
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pseudonimo',
            field=models.CharField(error_messages={'unique': 'Este pseudónimo ya está en uso.'}, max_length=100, unique=True, validators=[menu.models.validate_pseudonimo]),
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(error_messages={'unique': 'Ese email ya está en uso.'}, max_length=200, primary_key=True, serialize=False, validators=[menu.models.validate_correo]),
        ),
        migrations.AlterUniqueTogether(
            name='pedidoencuenta',
            unique_together=set([('plato', 'cuenta')]),
        ),
    ]
