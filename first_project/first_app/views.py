from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# each view should return HttpResponse
def index(request):
    my_dict = {'insert_me':"Hello, I am coming from first_app/index.html"}
    return render(request,'first_app/index.html',context=my_dict)
