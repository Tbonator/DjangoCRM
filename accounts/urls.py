from django.urls import path
from . import views

urlpatterns = [
    # url name use it to call in template rather than using full url name
    path('', views.home, name ='home'),
    path('products/', views.products,name = "products"),
    path('customer/<str:pk>/', views.customer,name="customer"),
]
