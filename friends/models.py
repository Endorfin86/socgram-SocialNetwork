from django.db import models
from django.contrib.auth.models import User

class UserFriends(models.Model):
    user = models.CharField('Инициатор', max_length=100)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Друг')

    def __str__(self):
        return f'{self.user} добавил в друзья {self.friend}'
    
    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'
