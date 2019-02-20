
from django.http import HttpResponse
from django.shortcuts import render, redirect
from login_regist_app.models import User
# Create your views here.

def regist(request):
    return render(request,'register.html')
def registlogic(request):
    username=request.POST.get('username')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    print(username,phone,email,pwd)
    User.objects.create(username=username,phone=phone,email_addr=email,password=pwd)
    return redirect('login_regist_app:login')
def usernameajax(request):
    username=request.GET.get('username')
    print(username)
    result=User.objects.filter(username=username)
    if result:
        return  HttpResponse('该用户名已注册')
    else:
        return HttpResponse('该用户名可用')