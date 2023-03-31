from django.contrib import admin
from .models import News
from .models import Likes, Comments

admin.site.register(News)
admin.site.register(Likes)
admin.site.register(Comments)
