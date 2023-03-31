from django.urls import path
from . import views
from django.contrib.auth import views as viewLogin
from django.contrib.auth import views as viewLogout

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.CustomLoginView.as_view(template_name='user/login.html'), name='log-in'),
    path('logout', viewLogout.LogoutView.as_view(template_name='user/logout.html'), name='log-out'),
    path('<str:username>', views.profile, name='profile'),
    path('del_post/', views.delpost),
    path('like/', views.like),
]