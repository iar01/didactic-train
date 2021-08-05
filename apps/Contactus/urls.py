from django.urls import path
from .Api import *

urlpatterns = [
    path('ContactUs', ContactAPI.as_view(), name='Contact us')
]
