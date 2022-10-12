from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<h1>My Second App</h1>")
# def help(request):
#     my_dict = {'insert_here':"I suppose to render in the help view"}
#     return render(request,'AppTwo/user.html',context=my_dict)

def user(request):
    users_list = User.objects.order_by('last_name')
    user_dict = {'users': users_list}
    return render(request, 'AppTwo/user.html', context=user_dict)
