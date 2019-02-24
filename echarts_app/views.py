from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from menu_app.models import Job
from redis import Redis

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
def zhexian(request):
    return render(request,'折线图.html')
def zhexianajax(request):
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
    return JsonResponse(data=data, safe=False)
def get_pie(request):
    return render(request,'pie.html')

def pie(request):
    py=Job.objects.filter(job_name__contains='python').count()
    pa=Job.objects.filter(job_name__contains='爬虫').count()
    da=Job.objects.filter(job_name__contains='大数据').count()
    ai=Job.objects.filter(job_name__contains='AI').count()
    data=[
        {'value': py , 'name': 'Python Web'},
        {'value': pa , 'name': '爬虫'},
        {'value': da , 'name': '大数据'},
        {'value': ai , 'name': 'AI'},
    ]
    return JsonResponse(data=data,safe=False)



def map(request):
    red = Redis(host='172.16.13.25', port=7000)
    data=[
                {"name": '北京',"value": 1},
                {"name": '天津',"value": 1},
                {"name": '上海',"value": 1},
                {"name": '重庆',"value": 1},
                {"name": '河北',"value": 1},
                {"name": '河南',"value": 1},
                {"name": '云南',"value": 1},
                {"name": '辽宁',"value": 1},
                {"name": '黑龙江',"value": 1},
                {"name": '湖南',"value": 1},
                {"name": '安徽',"value": 1},
                {"name": '山东',"value": 1},
                {"name": '新疆',"value": 1},
                {"name": '江苏',"value": 1},
                {"name": '浙江',"value": 1},
                {"name": '江西',"value": 1},
                {"name": '湖北',"value": 1},
                {"name": '广西',"value": 1},
                {"name": '甘肃',"value": 1},
                {"name": '山西',"value": 1},
                {"name": '内蒙古',"value": 1},
                {"name": '陕西',"value": 1},
                {"name": '吉林',"value": 1},
                {"name": '福建',"value": 1},
                {"name": '贵州',"value": 1},
                {"name": '广东',"value": 1},
                {"name": '青海',"value": 1},
                {"name": '西藏',"value": 1},
                {"name": '四川',"value": 1},
                {"name": '宁夏',"value": 1},
                {"name": '海南',"value": 1},
                {"name": '台湾',"value": 1},
                {"name": '香港',"value": 1},
                {"name": '澳门',"value": 1}
            ]
    for i in data:
        if red.zscore('addr', i['name']):
            i['value'] = red.zscore('addr', i['name'])
        else:
            i['value'] = 0
    return JsonResponse(data=data,safe=False)
def map_view(request):
    return render(request,'地图1.html')
