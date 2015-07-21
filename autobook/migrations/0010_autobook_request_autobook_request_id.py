# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0009_remove_autobook_request_autobook_request_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='autobook_request',
            name='autobook_request_id',
            field=models.CharField(default=datetime.datetime(2015, 7, 17, 6, 58, 43, 630222, tzinfo=utc), max_length=16),
            preserve_default=False,
        ),
    ]
