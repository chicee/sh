from django.contrib import admin

# Register your models here.
# admin에 Post 모델 추가하기! localhost:8000/admin
from .models import Post, Comment, Tag

class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 2 # stack처럼 쌓는 형식 -> 갯수

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','content','created_at',)
    list_display_links = ('id','created_at',)
    ordering = ('-id','-created_at')
    inlines = (CommentInlineAdmin,)
    list_filter = ('tags',)
    search_fields = ('content',)
    date_hierarchy = 'created_at'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
