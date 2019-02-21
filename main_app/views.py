from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def main_show(request):
    return render(request,'main.html')

def introduce_show(request):
    return render(request,'introduce.html')

def text(request):
    print(request.GET.get('resourceName'))
    return HttpResponse(request.GET.get('name'))

