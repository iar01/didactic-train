from django.urls import path
from .API import *

urlpatterns = [
    path('bundle/', BundleCreate.as_view(), name='Bundle Create'),
    path('bundle/<int:pk>/', BundleData.as_view(), name='Bundle RUD'),
]
