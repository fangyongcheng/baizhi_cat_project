from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from redis import Redis


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