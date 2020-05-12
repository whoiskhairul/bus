from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

from .bus import bus

def index(request):
    return render(request,'index.html')

def user_signup(request):
    form = UserCreationForm()
    return render(request,'signup.html',{'signup':form})

def user_login(request) :
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user:
            login(request,user)
            return render(request,'thank you.html')
        else :
            return HttpResponse("Username or Password Incorrect")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')



def show_user_info(request) :
    source = ''
    destination = ''
    context = {}
    if (request.method == 'POST') :
        source = request.POST['source']
        destination = request.POST['destination']
        context = bus(source,destination)

    return render(request,'bus_info.html', {'context' : context})



def show_bus_info(request,bus_name) :
    context = bus(bus_name)
    return render(request,'base.html',{'context':context, 'bus_name': bus_name.upper()})