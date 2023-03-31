from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat
from friends.models import UserFriends
from django.contrib.auth.models import User

@login_required
def chat(request, **kwargs):
    friend = kwargs['user']
    chat = Chat.objects.all()
    myfriends = UserFriends.objects.filter(user=request.user)
    thisfriend = User.objects.filter(username=kwargs['user']).first()
    return render(request, 'chat/chat.html', {'friend': friend, 'chat': chat, 'myfriends': myfriends, 'thisfriend': thisfriend})
