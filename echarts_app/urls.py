
from django.contrib import admin
from django.urls import path
from echarts_app import views
app_name='echarts_app'
urlpatterns = [
    path('map/',views.map,name='map' ),
    path('map_view/',views.map_view,name='map_view' ),
]
