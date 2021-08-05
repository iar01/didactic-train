from rest_framework import serializers
from .models import *


class BundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bundle
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'


class BundleDataSerializer(serializers.ModelSerializer):
    Point = PointSerializer(many=True)

    class Meta:
        model = Bundle
        fields = '__all__'
