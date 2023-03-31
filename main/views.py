from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import UserProfile
from news.models import News, Likes, Comments
from news.forms import CommentAdd
from django.contrib import messages


def home(request, **kwargs):
    profile = UserProfile.objects.filter(slug=request.user).first()
    news = News.objects.all().order_by('-id')
    comment = Comments.objects.all().order_by('-time')
    if request.method == 'POST':
        comformadd = CommentAdd(request.POST)
        if comformadd.is_valid():
            comformadd.save()
            newid = comformadd.cleaned_data.get('new')
            new = News.objects.get(pk=newid.pk)
            new.comment += 1
            new.save()
            return redirect('home')
    else:
        comformadd = CommentAdd()
    return render(request, 'main/home.html', {'profile': profile, 'news': news, 'comments': comment, 'comformadd': comformadd})

def api(request):
    return render(request, 'main/api.html')


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

def addcom(request, **kwargs):
    if request.method == 'POST':
        comformadd = CommentAdd(request.POST)
        if comformadd.is_valid():
            comformadd.save()
            newid = comformadd.cleaned_data.get('new')
            new = News.objects.get(pk=newid.pk)
            new.comment += 1
            new.save()
            return redirect('profile', request.user)

