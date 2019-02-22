from django.http import JsonResponse
from django.shortcuts import render
from menu_app.models import Job
# Create your views here.


def map(request):

    data_bj_pythonweb=Job.objects.filter(company_addr__contains="北京",job_name__contains='web').count()
    data_bj_pc=Job.objects.filter(company_addr__contains="北京",job_name__contains='爬虫').count()
    data_bj_dsj=Job.objects.filter(company_addr__contains="北京",job_name__contains='大数据').count()
    data_bj_ai=Job.objects.filter(company_addr__contains="北京",job_name__icontains ='ai').count()
    data_sh_pythonweb=Job.objects.filter(company_addr__contains="上海",job_name__contains='web').count()
    data_sh_pc=Job.objects.filter(company_addr__contains="上海",job_name__contains='爬虫').count()
    data_sh_dsj=Job.objects.filter(company_addr__contains="上海",job_name__contains='大数据').count()
    data_sh_ai=Job.objects.filter(company_addr__contains="上海",job_name__icontains ='ai').count()
    data_gz_pythonweb=Job.objects.filter(company_addr__contains="广州",job_name__contains='web').count()
    data_gz_pc=Job.objects.filter(company_addr__contains="广州",job_name__contains='爬虫').count()
    data_gz_dsj=Job.objects.filter(company_addr__contains="广州",job_name__contains='大数据').count()
    data_gz_ai=Job.objects.filter(company_addr__contains="广州",job_name__icontains ='ai').count()
    data_sz_pythonweb=Job.objects.filter(company_addr__contains="深圳",job_name__contains='web').count()
    data_sz_pc=Job.objects.filter(company_addr__contains="深圳",job_name__contains='爬虫').count()
    data_sz_dsj=Job.objects.filter(company_addr__contains="深圳",job_name__contains='大数据').count()
    data_sz_ai=Job.objects.filter(company_addr__contains="深圳",job_name__icontains ='ai').count()
    data=[data_bj_pythonweb,data_bj_pc,data_bj_dsj,data_bj_ai,data_sh_pythonweb,data_sh_pc,data_sh_dsj,data_sh_ai,
          data_gz_pythonweb,data_gz_pc,data_gz_dsj,data_gz_ai,data_sz_pythonweb,data_sz_pc,data_sz_dsj,data_sz_ai]
    return JsonResponse(data=data,safe=False)