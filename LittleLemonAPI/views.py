from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from . import serializers
from .models import MenuItem 
from rest_framework import generics
# Create your views here.
# class-based views
class MenuItemView(APIView):
	def get(self, request):
      return Response({"message":"single book with id "}, status.HTTP_200_OK)
	def put(self, request, pk):
      return Response({"title":"Oufaq"}, status.HTTP_200_OK)
    def post(self, request):
    	return Response({"title":"oufaq"}, status.HTTP_200_OK)
    def delete(self, request, pk):
    	return Response({"title":"oufaq"}, status.HTTP_200_OK) 
  
