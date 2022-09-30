from django.urls import path, re_path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
