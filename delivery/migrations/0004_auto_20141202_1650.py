# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_restaurante_coordenadas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='restaurante',
            name='longitud',
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='coordenadas',
            field=geoposition.fields.GeopositionField(max_length=42),
            preserve_default=True,
        ),
    ]
