from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import News
from user.models import UserProfile
from django.contrib.auth.models import User
from .forms import NewsAdd
from django.contrib import messages



