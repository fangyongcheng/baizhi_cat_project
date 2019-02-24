
from django.contrib import admin
from django.urls import path
from echarts_app import views
app_name='echarts_app'
urlpatterns = [
    path('map/',views.map,name='map' ),
    path('map_view/',views.map_view,name='map_view' ),
    path('bar/',views.bar,name='bar' ),
    path('barajax/',views.barajax,name='barajax' ),
    path('zhexian/',views.zhexian,name='zhexian'),
    path('zhexianajax/',views.zhexianajax,name='zhexianajax'),
    path('pie/',views.pie,name='pie' ),
    path('get_pie/',views.get_pie,name='get_pie' ),
    path('map/',views.map,name='map' ),
    path('map_view/',views.map_view,name='map_view' ),
]
