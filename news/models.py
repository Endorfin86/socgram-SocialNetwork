from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    text = models.TextField('Текст', null=True, blank=True)
    images = models.ImageField('Изображение', default='default-news.img', upload_to='news_images')
    files = models.FileField('Файл', default='default-news.file', upload_to='news_files')
    time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    athor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    like = models.IntegerField('Лайки', default=0)
    comment = models.IntegerField('Комментарии', default=0)

    def __str__(self):
        return f'Пост id-{self.pk} от {self.athor}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь лайк')
    new = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость лайк')

    def __str__(self):
        return f'{self.user} лайкнул {self.new}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

class Comments(models.Model):
    text = models.TextField('Комментарий')
    time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    new = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость')

    def __str__(self):
        return f'{self.user} прокомментировал {self.new}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'