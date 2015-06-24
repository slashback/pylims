# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20150607_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='registration_date',
            field=models.DateField(default=datetime.date(2015, 6, 23)),
            preserve_default=False,
        ),
    ]
