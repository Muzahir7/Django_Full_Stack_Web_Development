from django.urls import path
from signupApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),

]
