from rest_framework import serializers
from .models import UserFriends

class FriendsSerializer(serializers.ModelSerializer):
    '''вывод друзей'''
    friend = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = UserFriends
        fields = ('user', 'friend',)

class FriendCreateSerializer(serializers.ModelSerializer):
    '''создание друзей'''
    class Meta:
        model = UserFriends
        fields = "__all__"