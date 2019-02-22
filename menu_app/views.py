from django.core.paginator import Paginator
from django.shortcuts import render,redirect,HttpResponse
from main_app.captcha.image import ImageCaptcha
# Create your views here.
from menu_app.models import Job


CITYID=['','北京','上海','广州','深圳']

def menu_view(request):
    return render(request,'menu.html')

def menu_show_data(request):
    keyword = request.GET.get('keyword')
    page = request.GET.get('page')
    position_id = request.GET.get('position_id')
    flag=request.GET.get('flag')
    city_id = request.GET.get('city_id')
    if flag=='1' or flag =='2':
        if flag=="1":
            data = Job.objects.filter(company_addr__contains=keyword).values()
        else:
            data = Job.objects.filter(job_name__contains=keyword).values()
    else:
        if city_id == '':
            city_id = 1
        else:
            city_id = int(city_id)
        data = Job.objects.filter(job_name__contains=position_id).filter(
            company_addr__contains=CITYID[city_id]).values()
    if not page:
        page = 1
    else:
        page = int(page)
    pagtor = Paginator(data, per_page=10)
    try:
        data = pagtor.page(page)
    except:
        return render(request,'不是针对谁.html')
    else :
        page_count=divmod(pagtor.count,10)[0]
        if divmod(pagtor.count,10)[1] !=0:
            page_count+=1

        data_count=pagtor.count
        return render(request,'menu.html',
                      {"data":data,
                       'position_id':position_id,
                       'city_id':city_id,
                       "page_count":page_count,
                       "data_count":data_count,
                       "page":page,
                       "keyword":keyword,
                       "flag":flag,
                       })

def getcaptcha(request):
    try:
    #为验证码设置字体 获取当前目录下的xxx目录下的segoesc.ttf文件
        image = ImageCaptcha()
        keyword = request.GET.get('keyword')
        n = int(request.GET.get('n'))
        page = request.GET.get('page')
        position_id = request.GET.get('position_id')
        flag = request.GET.get('flag')
        city_id = request.GET.get('city_id')


        if flag == '1' or flag == '2':
            if flag == "1":
                data = Job.objects.filter(company_addr__contains=keyword).values()
            else:
                data = Job.objects.filter(job_name__contains=keyword).values()
        else:
            if city_id == '':
                city_id = 1
            else:
                city_id = int(city_id)
            data = Job.objects.filter(job_name__contains=position_id).filter(
                company_addr__contains=CITYID[city_id]).values()

        data=data[n]['salary']
        image = ImageCaptcha()

        #将生成的随机字符拼接成字符串，作为验证码图片中的文本
        data = image.generate(data )
    #写出验证图片 给客户端
        return HttpResponse(data, "image/png")
    except:
        return HttpResponse('1')