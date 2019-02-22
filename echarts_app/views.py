from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from menu_app.models import Job


def map(request):
    # return JsonResponse(data=data,safe=False)
    pass
def bar(request):
    return render(request,'柱状图.html')
def barajax(request):
    #四个城市的招聘数量对比
    number_beijing=len(Job.objects.filter(company_addr__contains='北京'))
    number_shanghai=len(Job.objects.filter(company_addr__contains='上海'))
    number_guangzhou=len(Job.objects.filter(company_addr__contains='广州'))
    number_shenzhen=len(Job.objects.filter(company_addr__contains='深圳'))
    data=[number_beijing,number_shanghai,number_guangzhou,number_shenzhen]
    return JsonResponse(data=data,safe=False)