"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from photos import views

urlpatterns = [
# r: raw! 문자그대로 표현하고자 씀. 즉 escaping 의 불편함 사라짐
# 첫번째인자 : url , 두번째인자 : View 함수 객체
# ^: 시작 / $:  끝

# /post/pk값/
# [0-9] --> 0부터 9까지 범위안에있는 모든 문자 1개
# [패턴]+ --> +는 한자리 이상
# [0-9]+ = /d 로도 표현가능
# ([패턴]) --> 소괄호로 발췌 --> View 함수 객체의 인자로 들어감
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login,
        {'template_name' : 'login.html'}, name = 'login_url'),
    url(r'^logout/$', logout,
        {'next_page': '/login/'}),
    url('', include('django.contrib.auth.urls')),
]
