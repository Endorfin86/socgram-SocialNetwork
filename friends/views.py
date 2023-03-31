from django.shortcuts import render, HttpResponse
from .models import UserFriends
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .serializers import FriendsSerializer, FriendCreateSerializer
from rest_framework.response import Response 

@login_required
def friends(request):
    friend = UserFriends.objects.filter(user=request.user)
    return render(request, 'friends/friends.html', {'friends': friend})

def addfriend(request):
    if request.GET:
        user = str(request.user)
        friend = request.GET['user_id']
        friends = UserFriends.objects.create(user=user, friend_id=friend)
        friends.save()
        return HttpResponse('yesplus')
    else:
        return HttpResponse('no')

def delfriend(request):
    if request.GET:
        user = request.user
        friend = request.GET['user_id']
        friends = UserFriends.objects.get(user=user, friend_id=friend)
        friends.delete()
        return HttpResponse('yesminus')
    else:
        return HttpResponse('no')

@login_required
def search(request, **kwargs):
    search = str(request.GET['search'])
    person = UserProfile.objects.all()
    usersearch = []
    nameshare = search.split(' ')
    for el in person:
        if el.firstname and el.lastname:
            namefull = el.firstname + ' ' + el.lastname
            if search.lower() in el.firstname.lower() or search.lower() in el.lastname.lower() or search.lower() == namefull.lower():
                usersearch.append(el)
            elif len(nameshare) > 1:
                if nameshare[0].lower() in el.firstname.lower() or nameshare[0].lower() in el.lastname.lower() or nameshare[1].lower() in el.firstname.lower() or nameshare[1].lower() in el.lastname.lower():
                    usersearch.append(el)
        else:
            pass

    count = f'Найдено: {len(usersearch)} записи'

    return render(request, 'friends/search.html', {'users': usersearch, 'count': count})

# API класс для вывода списка кто у кого в друзьях

class FriendsListView(APIView):
    '''вывод списка друзей'''
    def get(self, request):
        friends = UserFriends.objects.all()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data)

class FriendCreateView(APIView):
    '''создание друга'''
    def post(self, request):
        friend = FriendCreateSerializer(data=request.data)
        if friend.is_valid():
            friend.save()
            return Response(status=201)
