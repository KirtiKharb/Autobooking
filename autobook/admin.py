from django.contrib import admin

from .models import *

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('airline_id','airline_name')
admin.site.register(Airline, AirlineAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code','country_name')
admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_code','state_name','country')
admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('city_code','city_name','state','country')
admin.site.register(City, CityAdmin)

class AirportAdmin(admin.ModelAdmin):
    list_display = ('airport_code','airport_name','city','state','country')
admin.site.register(Airport, AirportAdmin)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id','source','destination','airline','arrival_at','departure_at','travel_type','economy_seats','business_seats','first_class_seats','economy_fare','business_fare','first_class_fare')
admin.site.register(Flight, FlightAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_email','first_name','last_name','gocash_balance','date_of_birth','nationality','street_address','city','state','country','pincode','mobile_number')
admin.site.register(User, UserAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id','flight_id','travel_class','number_of_passengers','total_cost','user_email')
admin.site.register(Booking, BookingAdmin)

class Autobook_requestAdmin(admin.ModelAdmin):
    list_display = ('autobook_request_id','user_email','source','destination','travel_class','number_of_passengers','maximum_price','minimum_price','date_of_flight')
admin.site.register(Autobook_request, Autobook_requestAdmin)