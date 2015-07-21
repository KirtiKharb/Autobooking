# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0008_auto_20150717_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autobook_request',
            name='autobook_request_id',
        ),
    ]
