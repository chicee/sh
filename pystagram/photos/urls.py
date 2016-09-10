from django.conf.urls import url
from . import views

app_name = 'photos'

# r: raw! 문자그대로 표현하고자 씀. 즉 escaping 의 불편함 사라짐
# 첫번째인자 : url , 두번째인자 : View 함수 객체
# ^: 시작 / $:  끝

# /post/pk값/
# [0-9] --> 0부터 9까지 범위안에있는 모든 문자 1개
# [패턴]+ --> +는 한자리 이상
# [0-9]+ = /d 로도 표현가능
# ([패턴]) --> 소괄호로 발췌 --> View 함수 객체의 인자로 들어감

urlpatterns = [
    url(r'^$', views.list_posts),
    url(r'^create/$', views.create_post, name='create'),
    url(r'^posts/(?P<pk>[0-9]+)/$',views.view_post, name='view_post'), #소괄호 안이 pk 인자로 전달
]
