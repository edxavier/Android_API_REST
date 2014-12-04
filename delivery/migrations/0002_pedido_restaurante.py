# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(default=1, to='delivery.Restaurante'),
            preserve_default=True,
        ),
    ]
