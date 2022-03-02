from dataclasses import fields
from pydoc import classname
from rest_framework  import serializers
from apps.users.models import User

# This allows complex structures and models from our Django project to be converted to native Python structures and can be converted to JSON or XML .

class UserSerializer(serializers.ModelSerializer): # Serializer to create, update and delele
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data): # I rewrite the base create function to encrypts the password when a user is created.
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data): # I rewrite the base update function to encrypts the password when a user is modified.
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer): # Serializer to list
    class Meta:
        model = User

    def to_representation(self, instance): # Only shows the chosen fields
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }