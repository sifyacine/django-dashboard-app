from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)  # Add the role field

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'confirm_password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        role = validated_data.pop('role')  # Get the role from the data
        user = User.objects.create_user(**validated_data)
        user.profile.role = role  # Assuming you have a profile model related to the user to store the role
        user.profile.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
