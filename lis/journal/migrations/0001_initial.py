# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('internal_nr', models.CharField(max_length='64')),
                ('state', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('state', models.IntegerField()),
                ('value', models.CharField(max_length='64')),
                ('measurement', models.ForeignKey(to='dictionary.Measurement')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('last_name', models.CharField(max_length='64', default='')),
                ('first_name', models.CharField(max_length='64', default='')),
                ('middle_name', models.CharField(max_length='64', default='')),
                ('gender', models.IntegerField()),
                ('birth_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('internal_nr', models.CharField(max_length='64')),
                ('state', models.IntegerField()),
                ('application', models.ForeignKey(to='journal.Application')),
                ('biomaterial', models.ForeignKey(to='dictionary.Biomaterial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='specimen',
            field=models.ForeignKey(to='journal.Specimen'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='patient',
            field=models.ForeignKey(to='journal.Patient'),
            preserve_default=True,
        ),
    ]
