from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def login(request):
    name=request.COOKIES.get('userid')
    pwd=request.COOKIES.get('psw')
    user=User.objects.filter(name=name,password=pwd)
    if user:
        request.session['flag'] = 'ok'   #记录下登录状态， OK时候登录，保持登录
        return redirect('列表页链接')
    else:
        return render(request, 'login.html')

def login_logic(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    user=User.objects.filter(name=name,password=pwd)
    if user:
        return HttpResponse('成功')
    else:
        return HttpResponse('用户名或密码错误！')

def login_ok(request):
    return redirect('列表页链接')








