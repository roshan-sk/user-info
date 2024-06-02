from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import userInfo
from .serializers import UserSerializer

@api_view(['GET'])
def getUser(request):
    data = userInfo.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response({"success": True, "message": "User details fetched successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def addUser(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True, "message": "User added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "message": "User creation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getOneUser(request, pk):
    try:
        user = userInfo.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response({"success": True, "message": "User details fetched successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    except userInfo.DoesNotExist:
        return Response({"success": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateUser(request, pk):
    try:
        user = userInfo.objects.get(pk=pk)
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "User details updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, "message": "Update failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except userInfo.DoesNotExist:
        return Response({"success": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteUser(request, pk):
    try:
        user = userInfo.objects.get(pk=pk)
        user.delete()
        return Response({"success": True, "message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except userInfo.DoesNotExist:
        return Response({"success": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)