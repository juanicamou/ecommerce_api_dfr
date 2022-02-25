from dataclasses import fields
from rest_framework  import serializers
from apps.users.models import User

# This allows complex structures and models from our Django project to be converted to native Python structures and can be converted to JSON or XML .

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'