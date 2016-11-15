# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161114_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_data',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
