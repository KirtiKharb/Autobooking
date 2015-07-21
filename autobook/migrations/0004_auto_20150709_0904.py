# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0003_auto_20150709_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='airline_name',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(to='autobook.Airline', to_field=b'airline_name'),
        ),
    ]
