from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: #
        model = Post # Post 에 있는 필드 정보들을 읽겠다. 자동으로 models의 필드를 전부 세팅해줌
        fields = '__all__'  #필드 전부 가져오겠다.
        # fields = ['user', 'title'] 안에 쓴것만 가져오겠다