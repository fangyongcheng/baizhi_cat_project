import re
import requests
from django.shortcuts import render,redirect,HttpResponse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from redis import Redis

from login_regist_app.models import User
# Create your views here.

url = "http://www.ip138.com/ips138.asp?ip=%s&action=2"
def login(request):
    name=request.COOKIES.get('userid')
    pwd=request.COOKIES.get('psw')
    user=User.objects.filter(username=name,password=pwd)
    if user:
        return redirect('main_app:main')
    else:
        return render(request, 'login.html')

def login_logic(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    user=User.objects.filter(username=name,password=pwd)
    if user:
        request.session['flag'] = 'ok'  # 记录下登录状态， OK时候登录，保持登录
        return HttpResponse('成功')
    else:
        return HttpResponse('用户名或密码错误！')

def login_ok(request):
    # redis保存
    res = requests.get(url % request.META["REMOTE_ADDR"])
    # res=request.META.get('REMOTE_ADDR')
    rule = '本站数据：(.*?) '
    rule = re.compile(rule)
    res.encoding = 'gb2312'
    addr = rule.findall(res.text)[0]
    if '市' in addr:
        addrs=addr.split('市')
    elif '省' in addr:
        addrs=addr.split('省')
    else:
        addrs=['北京','北京']
    red = Redis(host='172.16.13.25', port=7000)
    red.zincrby('addr',addrs[0],1)
    return redirect('main_app:main')




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