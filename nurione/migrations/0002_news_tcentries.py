# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nurione', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('news_key', models.CharField(max_length=50, null=True, blank=True)),
                ('src', models.CharField(max_length=10)),
                ('kind', models.CharField(max_length=3)),
                ('reg_date', models.DateTimeField(null=True, blank=True)),
                ('upt_date', models.DateTimeField(null=True, blank=True)),
                ('pub_yn', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('hitcnt', models.IntegerField()),
                ('youtube', models.CharField(max_length=60, null=True, blank=True)),
                ('path', models.CharField(max_length=15, null=True, blank=True)),
                ('thumbnail', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TcEntries',
            fields=[
                ('blogid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('draft', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('starred', models.IntegerField()),
                ('category', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('slogan', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('contentformatter', models.CharField(max_length=32, db_column='contentFormatter')),
                ('contenteditor', models.CharField(max_length=32, db_column='contentEditor')),
                ('location', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=32, null=True, blank=True)),
                ('acceptcomment', models.IntegerField(db_column='acceptComment')),
                ('accepttrackback', models.IntegerField(db_column='acceptTrackback')),
                ('published', models.IntegerField()),
                ('created', models.IntegerField()),
                ('modified', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('trackbacks', models.IntegerField()),
            ],
            options={
                'db_table': 'tc_Entries',
                'managed': False,
            },
        ),
    ]
