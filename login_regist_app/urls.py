from django.urls import path
from login_regist_app import views
app_name='login_regist_app'

urlpatterns=[
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('usernameajax/',views.usernameajax,name='usernameajax'),
]