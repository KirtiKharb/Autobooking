# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0010_autobook_request_autobook_request_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autobook_request',
            name='autobook_request_id',
        ),
    ]
