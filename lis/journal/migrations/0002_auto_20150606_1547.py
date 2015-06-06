# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20150606_1547'),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='division',
            field=models.ForeignKey(to='dictionary.Division', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='internal_nr',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='measurementresult',
            name='value',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=64, default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=64, default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(max_length=64, default=''),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='internal_nr',
            field=models.CharField(max_length=64),
        ),
    ]
