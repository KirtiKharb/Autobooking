from django.conf.urls import url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from autobook import views

urlpatterns = [
    # ex: /autobook/
    url(r'^$', views.home, name='home'),
    url(r'^flightDetails/$', views.flightDetails, name='flightDetails'),
    url(r'^autobookRequest/$', views.AutobookRequestListView.as_view(), name="AutobookRequestListView")
    
]
urlpatterns = format_suffix_patterns(urlpatterns)