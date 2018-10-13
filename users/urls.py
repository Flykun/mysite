from django.urls import path
from django.contrib.auth import login
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    # 登陆页面
    path('login/', login, 'users/login.html', name='login')
]
