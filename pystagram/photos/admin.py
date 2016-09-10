from django.contrib import admin

# Register your models here.
# admin에 Post 모델 추가하기! localhost:8000/admin
from .models import Post, Comment, Tag
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
