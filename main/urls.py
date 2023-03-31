from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api', views.api, name='api'),
    path('like/', views.like),
    path('addcom/', views.addcom, name='addcom')
]