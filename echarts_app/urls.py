
from django.contrib import admin
from django.urls import path
from login_regist_app import views
app_name='echarts_app.urls'
urlpatterns = [
    path('admin/', admin.site.urls),
]
