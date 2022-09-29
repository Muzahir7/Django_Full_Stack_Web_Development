from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# each view should return HttpResponse
def index(request):
    return HttpResponse("Hello World!")
