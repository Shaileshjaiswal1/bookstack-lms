from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('',views.base, name='base'),   
]