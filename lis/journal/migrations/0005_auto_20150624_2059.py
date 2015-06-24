# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_application_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.IntegerField(default=2, choices=[(0, 'Жен.'), (1, 'Муж'), (2, 'Не указано')]),
        ),
    ]
