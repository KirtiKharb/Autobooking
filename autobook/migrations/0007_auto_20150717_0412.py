# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0006_auto_20150710_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='airport_name',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='autobook_request',
            name='destination',
            field=models.ForeignKey(related_name='user_destination_airport', to='autobook.Airport', to_field=b'airport_name'),
        ),
        migrations.AlterField(
            model_name='autobook_request',
            name='source',
            field=models.ForeignKey(related_name='user_source_airport', to='autobook.Airport', to_field=b'airport_name'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(related_name='destination_airport', to='autobook.Airport', to_field=b'airport_name'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='source',
            field=models.ForeignKey(related_name='source_airport', to='autobook.Airport', to_field=b'airport_name'),
        ),
    ]
