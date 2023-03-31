from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_create(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, slug=instance)