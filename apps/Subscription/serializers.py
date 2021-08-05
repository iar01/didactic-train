from rest_framework import serializers

from .models import *
from ..QLA.serializer import SchoolSerializer, SubjectSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    Subject = SubjectSerializer()
    School = SchoolSerializer()

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'TimeStart', 'EndDate', 'Subject', 'School', 'PaymentMethod')


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
