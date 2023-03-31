from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistration, UserUpdate, UserProfileUpdate
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from news.models import News, Likes, Comments
from friends.models import UserFriends
from news.forms import NewsAdd
from django.contrib.auth.views import LoginView
from news.forms import CommentAdd


def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'user/registration.html', {'form': form})

# Переадресация пользователя после авторизации на страницу профиля example.com/user/endorfin86
class CustomLoginView(LoginView):
    def form_valid(self, form):
        self.success_url_kwargs = {'username': form.cleaned_data['username']}
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs=self.success_url_kwargs)

@login_required
def profile(request, **kwargs):
    user = User.objects.get(username=kwargs['username'])
    news = News.objects.filter(athor=user.pk).order_by('-time')
    profile = UserProfile.objects.filter(slug=kwargs['username']).first()
    like = Likes.objects.all().order_by('-id')
    friend = UserFriends.objects.filter(user=kwargs['username'])
    friendsall = UserFriends.objects.all()
    comment = Comments.objects.all().order_by('-time')
    coluser = len(User.objects.all())
    likeuser = len(Likes.objects.all())
    
    if request.method == 'POST':
        if len(request.POST) >= 9:
            form = UserUpdate(request.POST, instance=request.user)
            formprofile = UserProfileUpdate(request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid() and formprofile.is_valid():
                form.save()
                formprofile.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Страница пользователя {username} обновлена')
                return redirect('profile', username=request.user)
        elif len(request.POST) >= 3 and len(request.POST) <= 5:
            if request.method == 'POST':
                formadd = NewsAdd(request.POST, request.FILES)
                if formadd.is_valid():
                    formadd.save()
                    messages.success(request, f'Пост добавлен')
                    return redirect('profile', username=request.user)
    else:
        form = UserUpdate(instance=request.user)
        formprofile = UserProfileUpdate(instance=request.user.userprofile)
        formadd = NewsAdd()

    return render(request, 'user/profile.html', {
        'form': form, 
        'formprofile': formprofile, 
        'formadd': formadd,
        'comformadd': CommentAdd(),
        'comments': comment,
        'likes': like,
        'profile': profile, 
        'mynews': news, 
        'friends': friend,
        'friendsall': friendsall,
        'coluser': coluser,
        'likeuser': likeuser,
    })

def delpost(request):
    if request.GET:
        new = News.objects.filter(pk=request.GET['post_id'])
        new.delete()
        return HttpResponse('yes', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')

def like(request):
    if request.GET:
        new = News.objects.get(pk=request.GET['post_id'])
        try:
            like = Likes.objects.get(new=new.pk, user=request.user.pk)
            new.like -= 1
            new.save()
            like.delete()
            return HttpResponse('minus', content_type='text/html')
        except:
            like = Likes.objects.create(new_id=new.pk, user_id=request.user.pk)
            like.save()
            new.like += 1
            new.save() 
            return HttpResponse('plus', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')
