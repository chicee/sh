from django import forms
from .models import Post

class PostSimpleForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='내용', help_text = '글 내용은 200자 이하')
    tags = forms.CharField(required = False)

class PostForm(forms.ModelForm):
    tags = forms.CharField(required = False) # 이렇게 정의를 해주면 메타에서 안만들고이걸로 만듦
    class Meta:
        model = Post
        fields = ['content', 'tags'] # 따로정의안되어있으면 관계있는거끌어옴
