# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('subTotal', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to=b'menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('total', models.FloatField()),
                ('estado', models.CharField(max_length=30, choices=[(b'EN ESPERA', b'EN ESPERA'), (b'ATENDIENDOSE', b'ATENDIENDOSE'), (b'EN CAMINO', b'EN CAMINO'), (b'CANCELADO', b'CANCELADO'), (b'RECHAZADO', b'RECHAZADO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=11)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='menu',
            field=models.ForeignKey(to='delivery.Menu'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(to='delivery.Pedido'),
            preserve_default=True,
        ),
    ]
