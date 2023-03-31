from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from news.models import News


class UserRegistration(UserCreationForm):
    
    username = forms.CharField(
        required=True,
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )

    email = forms.EmailField(
        required=True,
        label='Почта',
        widget=forms.TextInput(attrs={'placeholder': 'Введите почту'})
    )

    password1 = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )

    password2 = forms.CharField(
        required=True,
        label='Пароль (повторно)',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdate(forms.ModelForm):
    
    username = forms.CharField(
        required=True,
        label='Логин',
    )

    email = forms.EmailField(
        required=True,
        label='Почта',
    )

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdate(forms.ModelForm):

    photo = forms.ImageField(label='Фото', required=False, widget=forms.FileInput())
    cover = forms.ImageField(label='Обложка', required=False, widget=forms.FileInput())

    class Meta:
        model = UserProfile
        fields = ['slug', 'firstname', 'lastname', 'status', 'phone', 'yourself', 'photo', 'cover']

