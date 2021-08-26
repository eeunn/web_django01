from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # 스크립트 안에 .editable을 사용하게 하기 위해 설정
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style': 'text-align: left;'
                                                                    'min-height: 10rem;'}))


    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']