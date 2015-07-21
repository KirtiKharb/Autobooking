from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from autobook.models import *
from autobook.serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#class flight(Views):

def home(request):
    if request.method=='GET':
        return render(request, 'autobook/home.html')

def flightDetails(request):
	flight_id = request.GET.get('flight_id')
	flight = get_object_or_404(Flight, flight_id=flight_id)
	return render(request, 'autobook/flightdetails.html', {'flight': flight})

class AutobookRequestListView(generics.ListCreateAPIView):

	model = Autobook_request
	serializer_class = Autobook_requestSerializer

	
	def get(self, request):
		flights = self.model.objects.all()
		serializer = self.serializer_class(flights, many=True)
		return Response(serializer.data)

	@method_decorator(csrf_exempt)
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class FlightListView(generics.ListCreateAPIView):
	serializer_class = FlightSerializer
	
	def get(self, request):
		flights = Flight.objects.filter(source=request.GET.get('source'), destination=request.GET.get('destination')).filter(departure_at__startswith=request.GET.get('date_of_flight'))
		serializer = self.serializer_class(flights, many=True)
		return Response(serializer.data)