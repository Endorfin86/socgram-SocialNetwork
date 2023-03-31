from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    message = models.TextField('Сообщение')
    sender = models.CharField('Отправитель', max_length=100)
    friend = models.CharField('Получатель', max_length=100)
    status = models.BooleanField('Статус сообщения', default=False)
    create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.sender} отправил сообщение {self.friend}'
    
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
