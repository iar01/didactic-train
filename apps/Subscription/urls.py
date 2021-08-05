from django.urls import path
from .api import *

urlpatterns = [
    path('getSubscription/', SubscriptionCheckAPI.as_view()),
    path('Subscription/', SubscriptionCreateView.as_view(), name='SubscriptionCreateView'),
    path('Subscription/<int:pk>/', GetDataView.as_view(), name='SubscriptionDataView'),

]
