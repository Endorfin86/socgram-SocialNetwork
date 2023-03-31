from django.shortcuts import render, redirect
from user.models import UserProfile
from news.models import Likes, Comments, News
from news.forms import CommentAdd
from django.contrib.auth.decorators import login_required

@login_required
def favorites(request, **kwargs):
    profile = UserProfile.objects.filter(slug=request.user).first()
    news = Likes.objects.filter(user=request.user)
    comment = Comments.objects.all().order_by('-time')
    if request.method == 'POST':
        comformadd = CommentAdd(request.POST)
        if comformadd.is_valid():
            comformadd.save()
            newid = comformadd.cleaned_data.get('new')
            new = News.objects.get(pk=newid.pk)
            new.comment += 1
            new.save()
            return redirect('favorites')
    else:
        comformadd = CommentAdd()
    return render(request, 'favorites/favorit.html', {'profile': profile, 'news': news, 'comments': comment, 'comformadd': comformadd})
