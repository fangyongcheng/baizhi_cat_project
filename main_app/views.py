from django.shortcuts import render,redirect,HttpResponse
import random,string
from main_app.captcha.image import ImageCaptcha
from menu_app.models import Job



# Create your views here.
def main_show(request):
    return render(request,'main.html')

def introduce_show(request):
    data_bj_pythonweb = Job.objects.filter(company_addr__contains="北京", job_name__icontains='web').count()
    data_bj_pc = Job.objects.filter(company_addr__contains="北京", job_name__contains='爬虫').count()
    data_bj_dsj = Job.objects.filter(company_addr__contains="北京", job_name__contains='数据').count()
    data_bj_ai = Job.objects.filter(company_addr__contains="北京", job_name__icontains='ai').count()
    data_sh_pythonweb = Job.objects.filter(company_addr__contains="上海", job_name__icontains='web').count()
    data_sh_pc = Job.objects.filter(company_addr__contains="上海", job_name__contains='爬虫').count()
    data_sh_dsj = len(Job.objects.filter(company_addr__contains="上海", job_name__contains='数据'))
    data_sh_ai = Job.objects.filter(company_addr__contains="上海", job_name__icontains='ai').count()
    data_gz_pythonweb = Job.objects.filter(company_addr__contains="广州", job_name__icontains='web').count()
    data_gz_pc = len(Job.objects.filter(company_addr__contains="广州", job_name__contains='爬虫'))
    data_gz_dsj = Job.objects.filter(company_addr__contains="广州", job_name__contains='数据').count()
    data_gz_ai = Job.objects.filter(company_addr__contains="广州", job_name__icontains='ai').count()
    data_sz_pythonweb = Job.objects.filter(company_addr__contains="深圳", job_name__icontains='web').count()
    data_sz_pc = Job.objects.filter(company_addr__contains="深圳", job_name__contains='爬虫').count()
    data_sz_dsj = Job.objects.filter(company_addr__contains="深圳", job_name__contains='数据').count()
    data_sz_ai = Job.objects.filter(company_addr__contains="深圳", job_name__icontains='ai').count()
    data = [data_bj_pythonweb, data_bj_pc, data_bj_dsj, data_bj_ai, data_sh_pythonweb, data_sh_pc, data_sh_dsj,
            data_sh_ai,
            data_gz_pythonweb, data_gz_pc, data_gz_dsj, data_gz_ai, data_sz_pythonweb, data_sz_pc, data_sz_dsj,
            data_sz_ai]
    print(data)
    return render(request,'introduce.html',{'data':data})

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






