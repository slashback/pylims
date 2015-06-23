# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20150606_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementresult',
            name='value',
            field=models.CharField(max_length=64, default=''),
        ),
    ]
