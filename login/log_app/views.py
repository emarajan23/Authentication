from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from .models import Device


def home(request):
    return render(request, 'log_app/home.html')


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
         form=UserCreationForm()
    return render (request,'log_app/register.html',{'form':form})


def device_list(request):
    devices = Device.objects.all()  
    return render(request, 'log_app/device_list.html', {'devices': devices})