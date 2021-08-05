from django.urls import path

from .api import *

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='User Profile'),
    path('UserDetail/', UserDetail.as_view(), name='User Detail'),
]
