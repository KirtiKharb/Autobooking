import datetime

from django.db import models
from django.utils import timezone
import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

class Airline(models.Model):
	airline_id = models.CharField(max_length=16, unique=True)
	airline_name = models.CharField(max_length=32, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.airline_name


class Country(models.Model):
	country_code = models.CharField(max_length=8, unique=True)
	country_name = models.CharField(max_length=32)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.country_name


class State(models.Model):
	state_code = models.CharField(max_length=8, unique=True)
	state_name = models.CharField(max_length=32)
	country = models.ForeignKey(Country, to_field = "country_code")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.state_name


class City(models.Model):
	city_code = models.CharField(max_length=8, unique=True)
	city_name = models.CharField(max_length=32)
	state = models.ForeignKey(State, to_field = "state_code")
	country = models.ForeignKey(Country, to_field = "country_code")	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.city_name


class Airport(models.Model):
	airport_code = models.CharField(max_length=16, unique=True)
	airport_name = models.CharField(max_length=64, unique=True)
	country = models.ForeignKey(Country, to_field = "country_code")
	state = models.ForeignKey(State, to_field = "state_code")
	city = models.ForeignKey(City, to_field = "city_code")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.airport_name


class Flight(models.Model):
	flight_id = models.CharField(max_length=16, unique=True)
	source = models.ForeignKey(Airport, to_field = "airport_code", related_name="source_airport")
	destination = models.ForeignKey(Airport, to_field = "airport_code", related_name="destination_airport")
	airline = models.ForeignKey(Airline, to_field = "airline_name")
	arrival_at = models.DateTimeField()
	departure_at = models.DateTimeField()
	travel_type = models.CharField(max_length=16)
	economy_seats = models.IntegerField(default=0)
	business_seats= models.IntegerField(default=0)
	first_class_seats= models.IntegerField(default=0)
	economy_fare= models.IntegerField(default=0)
	business_fare= models.IntegerField(default=0)
	first_class_fare= models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def  __str__(self):
		return self.flight_id


class User(models.Model):
	user_email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	gocash_balance = models.IntegerField()
	date_of_birth = models.DateField()
	nationality = models.CharField(max_length=16)
	street_address = models.TextField(max_length=64)
	city = models.CharField(max_length=32)
	state = models.CharField(max_length=32)
	country = models.CharField(max_length=32)
	pincode = models.IntegerField()
	mobile_number = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user_email


class Booking(models.Model):
	booking_id = models.CharField(max_length=32, unique=True)
	flight_id = models.ForeignKey(Flight, to_field = "flight_id")
	travel_class = models.CharField(max_length=16) 
	number_of_passengers = models.IntegerField(default=0)
	total_cost = models.IntegerField()
	user_email = models.ForeignKey(User, to_field = "user_email")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.booking_id


class Autobook_request(models.Model):
	autobook_request_id = models.CharField(max_length=16, default="Nil")

	user_email = models.ForeignKey(User, to_field = "user_email")
	source = models.ForeignKey(Airport, to_field = "airport_name", related_name="user_source_airport")
	destination = models.ForeignKey(Airport, to_field = "airport_name", related_name="user_destination_airport")
	travel_class = models.CharField(max_length=16)
	number_of_passengers = models.IntegerField(default=0)
	minimum_price = models.IntegerField()
	maximum_price = models.IntegerField()
	date_of_flight = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.autobook_request_id

	def save(self, *args, **kwargs):
		self.autobook_request_id = id_generator()
		print self.autobook_request_id
		super(Autobook_request, self).save(*args, **kwargs)	

