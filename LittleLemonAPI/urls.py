from django.urls import path
from . import views
 
    
  
urlpatterns = [
    path('menu-items/',views.MenuItemView.as_view()),
    path('menu-items/<str:title>',views.SingleMenuItemView.as_view()),
    path('category/',views.CategoryView.as_view()),
    path('orders/',views.OrderView.as_view()),
    path('orders/<str:user>',views.SingleOrderView.as_view()),
    path('cart/menu-items/<str:user>',views.SingleCartView.as_view()),
]


