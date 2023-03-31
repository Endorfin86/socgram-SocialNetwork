from django.db import models
from news.models import News

class UserFavorites(models.Model):
    new = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Понравившийся пост')

    def __str__(self):
        return f'Добавлен в избранное пост №{self.new.pk}'

    class Meta:
        verbose_name = 'Избранный пост'
        verbose_name_plural = 'Избранные посты'
