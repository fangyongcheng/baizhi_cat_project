from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def map(request):
    return JsonResponse(data=data,safe=False)