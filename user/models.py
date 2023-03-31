from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class UserProfile(models.Model):
    slug = models.SlugField('Идентификатор', unique=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    firstname = models.CharField('Имя', max_length=100, null=True, blank=True)
    lastname = models.CharField('Фамилия', max_length=100, null=True, blank=True)
    status = models.CharField('Статус', max_length=255, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=12, null=True, blank=True)
    yourself = models.TextField('О себе', null=True, blank=True)
    photo = models.ImageField('Фото', default='default-photo.png', upload_to='user_photo', null=True, blank=True)
    cover = models.ImageField('Обложка', default='default-cover.png', upload_to='user_cover', null=True, blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user})

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.cover.path)
        if image.height > 150 and image.width > 1000:
            h = (image.height - 300) / 2
            hh = h + 300
            w = (image.width - 1000) / 2
            ww = w + 1000
            cover_size = image.crop((w, h, ww, hh))
            cover_size.save(self.cover.path)

        # photo = Image.open(self.photo.path)
        # if photo.height > 250 and photo.width > 250:
        #     hp = (photo.height - 250) / 2
        #     hhp = hp + 250
        #     wp = (photo.width - 250) / 2
        #     wwp = wp + 250
        #     photo_size = photo.crop((wp, hp, wwp, hhp))
        #     photo_size.save(self.photo.path)

        # photo = Image.open(self.photo.path)
        # if photo.height > 250 and photo.width > 250:
        #     hp = siz

        #     wp = (photo.width - 250) / 2
        #     wwp = wp + 250
        #     photo_size = photo.crop((wp, hp, wwp, hhp))
        #     photo_size.save(self.photo.path)


        photo = Image.open(self.photo.path)
        if photo.height > photo.width:
            fix = 250
            procent = photo.height / photo.width
            height = int(fix * float(procent))
            new_image = photo.resize((fix, height))
            new_image.save(self.photo.path)
            photo = Image.open(self.photo.path)
            width = photo.width
            h = (photo.height - 250) / 2
            hh = h + 250
            photo_size = photo.crop((0, h, width, hh))
            photo_size.save(self.photo.path)


        elif photo.width > photo.height:
            fix = 250
            procent = photo.width / photo.height
            width = int(fix * float(procent))
            new_image = photo.resize((width, fix))
            new_image.save(self.photo.path)
            photo = Image.open(self.photo.path)
            height = photo.height
            w = (photo.width - 250) / 2
            ww = w + 250
            photo_size = photo.crop((w, 0, ww, height))
            photo_size.save(self.photo.path)
        
        else:
            new_image = photo.resize((250, 250))
            new_image.save(self.photo.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
