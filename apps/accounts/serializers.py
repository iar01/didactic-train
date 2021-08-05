from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'firstname', 'lastname', 'pic', 'School', 'type_of_user')


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'username', 'firstname', 'lastname', 'is_active', 'pic', 'School',
            'is_staff', 'AccountOwner')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'firstname', 'lastname', 'password', 'School', 'Country')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validate_data):
            user = User.objects.create_user(
                validate_data['email'],
                validate_data['firstname'],
                validate_data['lastname'],
                validate_data['password'],
                validate_data['School'],
                validate_data['Country'],
            )
            return user


class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class ChangePassword(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
