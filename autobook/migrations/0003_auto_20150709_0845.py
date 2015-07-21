# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0002_auto_20150709_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 44, 54, 930564, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 44, 59, 833708, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autobook_request',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 3, 354781, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autobook_request',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 6, 897807, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 12, 942202, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 16, 251934, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 19, 542898, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 23, 196056, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 25, 945527, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 29, 207621, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 32, 47804, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 34, 760839, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 37, 293500, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 40, 74539, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 45, 477286, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 9, 8, 45, 57, 418127, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='airline',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
