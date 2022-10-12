from django.shortcuts import render
# from django.http import HttpResponse
# from signupApp.models import User
from signupApp.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'signupApp/index.html')


def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'signupApp/users.html', {'form':form})
