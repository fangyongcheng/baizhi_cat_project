from django.shortcuts import render,redirect,HttpResponse
import random,string
from main_app.captcha.image import ImageCaptcha




# Create your views here.
def main_show(request):
    return render(request,'main.html')

def introduce_show(request):
    return render(request,'introduce.html')

def text(request):
    print(request.GET.get('resourceName'))
    return HttpResponse(request.GET.get('name'))



#验证码验证    隔10min验证一次

def captcha_url(request):
    return render(request,'captcha.html')


def getcaptcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters + string.digits, 4)
    code = ''.join(code)
    print(code)
    request.session['code'] = code
    data = image.generate(code)
    return HttpResponse(data, 'image/png')


def check_captcha(request):
    code_num=request.GET.get('code_id')
    code=request.session.get('code')
    if code.lower() == code_num.lower():
        return redirect('main_app:main')
    else:
        return render(request,'captcha.html')






