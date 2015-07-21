# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acID', models.IntegerField(default=0)),
                ('acNumber', models.CharField(max_length=32)),
                ('capacity', models.IntegerField(default=0)),
                ('mfdBy', models.CharField(max_length=64)),
                ('mfdOn', models.DateTimeField(verbose_name=b'date manufactured')),
            ],
        ),
        migrations.CreateModel(
            name='AirFare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afID', models.IntegerField(default=0)),
                ('fare', models.IntegerField(default=0)),
                ('fsc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chID', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=32)),
                ('amount', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnID', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=16)),
                ('cell', models.CharField(max_length=16)),
                ('tel', models.CharField(max_length=16)),
                ('street', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ctID', models.IntegerField(default=0)),
                ('countryName', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diID', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=32)),
                ('amount', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flID', models.IntegerField(default=0)),
                ('flightDate', models.DateTimeField(verbose_name=b'Flight Date')),
                ('departure', models.DateTimeField(verbose_name=b'Departure Date')),
                ('arrival', models.DateTimeField(verbose_name=b'Arrival Date')),
                ('aircraft', models.ForeignKey(to='autobook.Aircraft')),
                ('netFare', models.ForeignKey(to='autobook.AirFare')),
            ],
        ),
        migrations.CreateModel(
            name='PassengerDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('psID', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=64)),
                ('nationalities', models.CharField(max_length=16)),
                ('contacts', models.ForeignKey(to='autobook.ContactDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rtID', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=32)),
                ('destination', models.CharField(max_length=32)),
                ('routeCode', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stID', models.IntegerField(default=0)),
                ('stateName', models.CharField(max_length=32)),
                ('country', models.ForeignKey(to='autobook.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tsID', models.IntegerField(default=0)),
                ('bookingDate', models.DateTimeField(verbose_name=b'Booking Date')),
                ('departureDate', models.DateTimeField(verbose_name=b'Departure Date')),
                ('type_s', models.CharField(max_length=1)),
                ('total', models.IntegerField(default=0)),
                ('charges', models.ForeignKey(to='autobook.Charges')),
                ('discount', models.ForeignKey(to='autobook.Discount')),
                ('flight', models.ForeignKey(to='autobook.FlightSchedule')),
                ('passenger', models.ForeignKey(to='autobook.PassengerDetails')),
            ],
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='state',
            field=models.ForeignKey(to='autobook.State'),
        ),
        migrations.AddField(
            model_name='airfare',
            name='route',
            field=models.ForeignKey(to='autobook.Route'),
        ),
    ]
