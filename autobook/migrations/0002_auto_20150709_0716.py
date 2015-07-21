# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autobook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('airline_id', models.CharField(unique=True, max_length=16)),
                ('airline_name', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('airport_code', models.CharField(unique=True, max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Autobook_request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autobook_request_id', models.CharField(unique=True, max_length=32)),
                ('travel_class', models.CharField(max_length=16)),
                ('number_of_passengers', models.IntegerField(default=0)),
                ('minimum_price', models.IntegerField()),
                ('maximum_price', models.IntegerField()),
                ('date_of_flight', models.DateField()),
                ('destination', models.ForeignKey(related_name='user_destination_airport', to='autobook.Airport', to_field=b'airport_code')),
                ('source', models.ForeignKey(related_name='user_source_airport', to='autobook.Airport', to_field=b'airport_code')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_id', models.CharField(unique=True, max_length=32)),
                ('travel_class', models.CharField(max_length=16)),
                ('number_of_passengers', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_code', models.CharField(unique=True, max_length=8)),
                ('city_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_id', models.CharField(unique=True, max_length=16)),
                ('arrival_at', models.DateTimeField()),
                ('departure_at', models.DateTimeField()),
                ('travel_type', models.CharField(max_length=16)),
                ('economy_seats', models.IntegerField(default=0)),
                ('business_seats', models.IntegerField(default=0)),
                ('first_class_seats', models.IntegerField(default=0)),
                ('economy_fare', models.IntegerField(default=0)),
                ('business_fare', models.IntegerField(default=0)),
                ('first_class_fare', models.IntegerField(default=0)),
                ('airline', models.ForeignKey(to='autobook.Airline', to_field=b'airline_id')),
                ('destination', models.ForeignKey(related_name='destination_airport', to='autobook.Airport', to_field=b'airport_code')),
                ('source', models.ForeignKey(related_name='source_airport', to='autobook.Airport', to_field=b'airport_code')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(unique=True, max_length=16)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('gocash_balance', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=16)),
                ('street_address', models.TextField(max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('pincode', models.IntegerField()),
                ('mobile_number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='airfare',
            name='route',
        ),
        migrations.RemoveField(
            model_name='contactdetails',
            name='state',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='aircraft',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='netFare',
        ),
        migrations.RemoveField(
            model_name='passengerdetails',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='charges',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='passenger',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='countryName',
            new_name='country_name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='stateName',
            new_name='state_name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='ctID',
        ),
        migrations.RemoveField(
            model_name='state',
            name='stID',
        ),
        migrations.AddField(
            model_name='country',
            name='country_code',
            field=models.CharField(default=datetime.datetime(2015, 7, 9, 7, 16, 25, 798079, tzinfo=utc), unique=True, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='state_code',
            field=models.CharField(default=datetime.datetime(2015, 7, 9, 7, 16, 46, 225908, tzinfo=utc), unique=True, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(to='autobook.Country', to_field=b'country_code'),
        ),
        migrations.DeleteModel(
            name='Aircraft',
        ),
        migrations.DeleteModel(
            name='AirFare',
        ),
        migrations.DeleteModel(
            name='Charges',
        ),
        migrations.DeleteModel(
            name='ContactDetails',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='FlightSchedule',
        ),
        migrations.DeleteModel(
            name='PassengerDetails',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='autobook.Country', to_field=b'country_code'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='autobook.State', to_field=b'state_code'),
        ),
        migrations.AddField(
            model_name='booking',
            name='flight_id',
            field=models.ForeignKey(to='autobook.Flight', to_field=b'flight_id'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_email',
            field=models.ForeignKey(to='autobook.User', to_field=b'user_email'),
        ),
        migrations.AddField(
            model_name='autobook_request',
            name='user_email',
            field=models.ForeignKey(to='autobook.User', to_field=b'user_email'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(to='autobook.City', to_field=b'city_code'),
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(to='autobook.Country', to_field=b'country_code'),
        ),
        migrations.AddField(
            model_name='airport',
            name='state',
            field=models.ForeignKey(to='autobook.State', to_field=b'state_code'),
        ),
    ]
