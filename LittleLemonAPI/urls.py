from django.urls import path
from .views import MenuItemView ,SingleMenuItemView
 
    
  
urlpatterns = [
     path('menu-items/',MenuItemView.as_view()),
     path('menu-items/<str:title>',SingleMenuItemView.as_view()),

   
]


