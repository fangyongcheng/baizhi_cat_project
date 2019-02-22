
from django.contrib import admin
from django.urls import path
from echarts_app import views
app_name='echarts_app.urls'
urlpatterns = [
    path('map/',views.map,name='map' ),
]
