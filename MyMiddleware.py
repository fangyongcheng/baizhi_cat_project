from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MyMiddleAware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)


    # view处理请求前执行
    def process_request(self, request):
        user = request.META.get('HTTP_USER_AGENT')
        ip = request.META.get('REMOTE_ADDR')
        ip1= request.META.get('HTTP_X_FORWARDED_FOR')
        # print('user-agent', user)
        # print('ip', ip,'####',ip1)
        if 'Windows' in user or 'Mac' in user:
            pass
            # print("request:", request)
        else :
            return render(request,'404.html')

    # 在process_request之后View之前执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print("view:", request, view_func, view_args, view_kwargs)
        pass
    # view执行之后，响应之前执行
    def process_response(self, request, response):
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)
