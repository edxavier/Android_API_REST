# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_pedido_restaurante'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='coordenadas',
            field=geoposition.fields.GeopositionField(default=None, max_length=42),
            preserve_default=True,
        ),
    ]
