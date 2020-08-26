from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegisterForm()
    return render(request,'login/register.html',{'form':form})

def loginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return HttpResponse("Welcome")
        else:
            print("username or password is incorrect ")
    context={}
    return render(request,'login/login.html')
