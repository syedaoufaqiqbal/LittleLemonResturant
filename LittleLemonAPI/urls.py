from django.urls import path
from .views import views 

urlpatterns = [
    path('menu-item/', views.ListUsers.as_view()),
    #path('menu-item/<int:pk>',views.MenuItemView.as_view())
]

