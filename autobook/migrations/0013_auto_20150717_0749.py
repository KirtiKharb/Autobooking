# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0012_autobook_request_autobook_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autobook_request',
            name='autobook_request_id',
            field=models.CharField(default=b'Nil', max_length=16),
        ),
    ]
