from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDetails
from .Serializers import SeralizedUser
# Create your views here.

@api_view(['GET'])
def get_user(request):
    user_data = UserDetails.objects.all()
    serializer = SeralizedUser(user_data, many=True)
    return Response(serializer, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    serializer = SeralizedUser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request, pk):
    user = UserDetails.objects.get(pk=pk)
    serializer = SeralizedUser(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    user = UserDetails.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)