from django.urls import path
from . import views

urlpatterns = [
    # url name use it to call in template rather than using full url name
      path('register/', views.registerPage, name ='register'),
      path('login/', views.loginPage, name ='login'),
    
    
    path('', views.home, name ='home'),
    path('products/', views.products,name = "products"),
    path('customer/<str:pk>/', views.customer,name="customer"),
    
    path('create_order/<str:pk>/',views.createOrder,name="create_order"),
    path('update_order/<str:pk>/',views.updaterOrder,name="update_order"),
    path('delete_order/<str:pk>/',views.deleteOrder,name="delete_order"),
    
    
]
