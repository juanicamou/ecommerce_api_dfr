from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET'])
def user_get_all_api_view(request): # Returns all users
    if request.method == 'GET': 
        users = User.objects.all() # Brings all objects
        users_serializer = UserSerializer(users, many = True) # Tranforms model object in json (Serializer task)
        return Response(users_serializer.data) # Returns the json response

@api_view(['POST'])
def user_create_api_view(request): # Creates a new user
    if request.method == 'POST': 
        user_serializer = UserSerializer(data = request.data) # Tranforms json in model object (Serializer task)
        if user_serializer.is_valid(): # Checks if the request data is valid with model 
            user_serializer.save() # Saves the object
            return Response(user_serializer.data) # Returns a json response with creation information
        return Response(user_serializer.errors) # Returns a json response with the error information


@api_view(['GET'])
def user_detail_api_view(request, pk):
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
