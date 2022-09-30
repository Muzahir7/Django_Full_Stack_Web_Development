from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>My Second App</h1>")
def help(request):
    my_dict = {'insert_here':"I suppose to render in the help view"}
    return render(request,'AppTwo/help.html',context=my_dict)
