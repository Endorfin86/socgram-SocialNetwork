from news.models import News, Comments
from django import forms

class NewsAdd(forms.ModelForm):

    text = forms.CharField(
        required=False,
        label='Текст',
        widget=forms.Textarea(attrs={'placeholder': 'Что у вас нового?'})
    )
    
    class Meta:
        model = News
        fields = ['text', 'images', 'files', 'athor']

class CommentAdd(forms.ModelForm):

    text = forms.CharField(
        required=True,
        label='Комментарий',
        widget=forms.Textarea(attrs={'placeholder': 'Что вы об этом думаете...'})
    )
    
    class Meta:
        model = Comments
        fields = ['text', 'user', 'new']


