from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET'])
def user_get_all_api_view(request): # Returns all users
    users = User.objects.all() # Brings all objects
    users_serializer = UserSerializer(users, many = True) # Tranforms model object in json (Serializer task)
    return Response(users_serializer.data, status = status.HTTP_200_OK) # Returns the json response

@api_view(['POST'])
def user_create_api_view(request): # Creates a new user
    user_serializer = UserSerializer(data = request.data) # Tranforms json in model object (Serializer task)
    if user_serializer.is_valid(): # Checks if the request data is valid with model 
        user_serializer.save() # Saves the object
        return Response(user_serializer.data, status = status.HTTP_201_CREATED) # Returns a json response with creation information
    return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST) # Returns a json response with the error information


@api_view(['GET'])
def user_detail_api_view(request, pk): # Shows the detail of a user
    user = User.objects.filter(id = pk).first() # Brings the object
    if user:
        user_serializer = UserSerializer(user) # Tranforms model object in json (Serializer task)
        return Response(user_serializer.data, status = status.HTTP_200_OK) # Returns the json response
    return Response({'message': 'A user with the input data has not been found.'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_update_api_view(request, pk): # Updates an user
    user = User.objects.filter(id = pk).first() # Brings the object
    if user:
        user_serializer = UserSerializer(user, data = request.data) # Tranforms json in model object (Serializer task)
        if user_serializer.is_valid(): # Checks if the request data is valid with model 
            user_serializer.save() # Saves the object
            return Response(user_serializer.data, status = status.HTTP_200_OK) # Returns a json response with modification information
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)  # Returns a json response with the error information
    return Response({'message': 'A user with the input data has not been found.'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def user_delete_api_view(request, pk): # Deletes an user
    user = User.objects.filter(id = pk).first() # Brings the object
    if user:
        user.delete() # Deletes the user
        return Response({'message': 'The user was deleted successfully'}, status = status.HTTP_200_OK)
    return Response({'message': 'A user with the input data has not been found.'}, status = status.HTTP_400_BAD_REQUEST)