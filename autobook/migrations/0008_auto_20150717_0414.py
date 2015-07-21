# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0007_auto_20150717_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(related_name='destination_airport', to='autobook.Airport', to_field=b'airport_code'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='source',
            field=models.ForeignKey(related_name='source_airport', to='autobook.Airport', to_field=b'airport_code'),
        ),
    ]
