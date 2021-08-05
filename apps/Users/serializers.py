from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'date_of_birth', 'firstname', 'lastname', 'is_active', 'pic', 'School', 'is_staff',
                  'AccountOwner', 'created_at', 'updated_at']


class CompactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'firstname', 'lastname', 'pic', 'School']
