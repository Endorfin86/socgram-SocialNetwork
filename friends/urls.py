from django.urls import path
from . import views


urlpatterns = [
    path('', views.friends, name='friends'),
    path('search', views.search, name='search'),
    path('add', views.addfriend),
    path('del', views.delfriend),

    # API запросы
    path('list', views.FriendsListView.as_view()),
    path('create', views.FriendCreateView.as_view())
]