from django.forms import widgets
from rest_framework import serializers
from autobook.models import *

class AirlineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Airline
		fields =  ('airline_id', 'airline_name')

class FlightSerializer(serializers.ModelSerializer):          
	class Meta:         
		model = Flight                 
		fields = ('flight_id', 'source', 'destination', 'airline', 'arrival_at', 'departure_at', 'travel_type', 'economy_seats', 'business_seats', 'first_class_seats', 'economy_fare', 'business_fare', 'first_class_fare')

class Autobook_requestSerializer(serializers.ModelSerializer):

	class Meta:
		model = Autobook_request
		read_only_fields = ('autobook_request_id',)