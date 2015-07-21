# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0004_auto_20150709_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='airport_name',
            field=models.CharField(default=datetime.datetime(2015, 7, 9, 10, 36, 39, 643483, tzinfo=utc), max_length=64),
            preserve_default=False,
        ),
    ]
