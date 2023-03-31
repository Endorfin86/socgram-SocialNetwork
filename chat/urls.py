from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>', views.chat, name='chat'),
]