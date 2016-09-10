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
from django.contrib import admin

from photos import views

urlpatterns = [
# r: raw! 문자그대로 표현하고자 씀. 즉 escaping 의 불편함 사라짐
# 첫번째인자 : url , 두번째인자 : View 함수 객체
# ^: 시작 / $:  끝
    url(r'^$', views.list_posts),
    url(r'^hello/$', views.hello_world),
    url(r'^admin/', admin.site.urls),
]
