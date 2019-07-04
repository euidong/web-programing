
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 20)
    first_name = serializers.CharField(max_length= 10)
    last_name = serializers.CharField(max_length = 10)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.url)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

