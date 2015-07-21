# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0005_airport_airport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
