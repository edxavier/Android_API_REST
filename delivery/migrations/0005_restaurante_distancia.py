# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_auto_20141202_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='distancia',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
