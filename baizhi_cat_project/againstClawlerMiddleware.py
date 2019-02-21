import time
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MyMiddleAware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        self.ips={}
        self.time_count=time.time()+60
    # view处理请求前执行
    def process_request(self, request):
        if request.META["HTTP_HOST"] in self.ips:
            self.ips[request.META["HTTP_HOST"]]+=1
            if self.ips[request.META["HTTP_HOST"]]>=10:
                if self.time_count<time.time():
                    self.time_count = time.time() + 60
                    self.ips={}
                return render(request,'crawler_error.html')

        else:
            self.ips[request.META["HTTP_HOST"]]=1

