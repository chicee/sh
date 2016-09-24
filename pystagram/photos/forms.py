from django import forms
from django.forms import ValidationError

from .models import Post

class PostSimpleForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='내용', help_text = '글 내용은 200자 이하')
    tags = forms.CharField(required = False)

class PostForm(forms.ModelForm):
    tags = forms.CharField(required = False) # 이렇게 정의를 해주면 메타에서 안만들고이걸로 만듦
    class Meta:
        model = Post
        fields = ['content', 'tags'] # 따로정의안되어있으면 관계있는거끌어옴

    def clean_content(self):
        content = self.cleaned_data['content']
        if '바보' in content:
            _msg = '본문에 금지어가 있습니다 : {}'.format('바보')
            # self.add_error('content', _msg)
            raise ValidationError(_msg) # 엄격하게 여기서 멈춤
        return content # 주의! 반드시 정제된 결과를 리턴 해야함

    def clean(self):
        content = self.cleaned_data.get('content')
        if content and '띨띨이' in content:
            _msg = '방심하지마라! 금지어 있다: {}'.format('띨띨이')
            self.add_error('content', _msg)
