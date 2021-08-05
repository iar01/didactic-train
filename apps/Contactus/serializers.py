from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    model = Contactus
    fields = '__all__'
