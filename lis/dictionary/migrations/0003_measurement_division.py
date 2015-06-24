# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20150606_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='division',
            field=models.ForeignKey(default=1, to='dictionary.Division'),
            preserve_default=False,
        ),
    ]
