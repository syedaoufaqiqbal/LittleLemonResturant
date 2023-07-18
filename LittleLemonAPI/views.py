from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .models import MenuItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from rest_framework import generics
from .serializers import MenuItemSerializers
""" from .models import MenuItem 
from rest_framework import authentication, permissions
from rest_framework import generics """
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
         
          """ 
class MenuItemView(APIView):
      def get(self,request):
          Menues=MenuItem.objects.all()
          return Response(Menues)
      
      def get(self,request,menuItem):
        Menues=MenuItem.objects.all()
        return Response(Menues.values()) """
      
""" @api_view(['GET','POST'])      
def menu_items(request):
    if request.method=='GET':
        items=MenuItem.objects.all()
        serialize_menues= MenuItemSerializers(items,many="true")
        return Response(serialize_menues.data)
    if request.method=='POST':
        serialized_item=MenuItemSerializers(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data,status.HTTP_201_CREATED)
          
@api_view      
def single_items(request,item):
    items=get_object_or_404(MenuItem,title=item)
    serialize_menues= MenuItemSerializers(items)
    return Response(serialize_menues.data)
                """
class MenuItemView(generics.ListCreateAPIView):
 queryset = MenuItem.object.all()
 serializer_class = MenuItemSerializers
 permission_classes = [IsAuthenticated]
 
class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.object.all()
    serializer_class = MenuItemSerializers
    permission_classes = [IsAuthenticated]