from django.urls import path
from . import views 
from . import views
urlpatterns = [
    path('menu-item/', views.ListUsers.as_view()),
   
]

