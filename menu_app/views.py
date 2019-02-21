from django.core.paginator import Paginator
from django.shortcuts import render,redirect

# Create your views here.
from menu_app.models import Job

CITYID=['','北京','上海','广州','深圳']

def menu_view(request):
    return render(request,'menu.html')

def menu_show_data(request):
    position_id=request.GET.get('position_id')
    city_id=request.GET.get('city_id')
    page=request.GET.get('page')
    if not city_id:
        city_id=1
    else:
        city_id=int(city_id)
    if not page:
        page=1
    else:
        page=int(page)
    data=Job.objects.filter(job_name__contains=position_id).filter(company_addr__contains=CITYID[city_id]).values()
    pagtor = Paginator(data, per_page=10)
    data = pagtor.page(page)
    page_count=int(pagtor.count/10+0.5)
    return render(request,'menu.html',{"data":data,'position_id':position_id,'city_id':city_id,"page_count":page_count})

