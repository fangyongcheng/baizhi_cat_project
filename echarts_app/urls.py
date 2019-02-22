
from django.contrib import admin
from django.urls import path
from echarts_app import views
app_name='echarts_app'
urlpatterns = [
    path('map/',views.map,name='map' ),
    path('bar/',views.bar,name='bar' ),
    path('barajax/',views.barajax,name='barajax' ),
]
