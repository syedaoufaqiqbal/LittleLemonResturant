from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from . import serializers
from .models import MenuItem 
from rest_framework import authentication, permissions
from rest_framework import generics
from django.contrib.auth.models import User
# Create your views here.
# class-based views
""" class MenuItemView(APIView):
    def get(self, request, pk):
     return Response({"message"}, status.HTTP_200_OK)
	def put(self, request, pk):
    	return Response({"title":request.data.get('title')}, status.HTTP_200_OK) """
     
class ListUsers(APIView):
      def get(self, request, format=None):
          usernames = [user.username for user in User.objects.all()]
          return Response(usernames)

       