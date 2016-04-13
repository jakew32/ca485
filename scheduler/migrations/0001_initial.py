# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('event_date', models.DateField(verbose_name=b'date of the event')),
                ('time_start', models.TimeField(verbose_name=b'start time of the event')),
                ('time_end', models.TimeField(verbose_name=b'end time of the event')),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('time_start', models.TimeField(verbose_name=b'start time of the subevent')),
                ('duration', models.IntegerField(verbose_name=b'number of minutes for the subevent slot')),
                ('description', models.TextField()),
                ('event_id', models.ForeignKey(to='scheduler.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
