from rest_framework import serializers
from .models import BandRequest, Friends1, Musician

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id', 'aboutMe', 'instruments', 'influences', 'genres', 'video', 'user_id']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends1
        fields = ['users1', 'curent_user']

class BandRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandRequest
        fields = ['sender', 'receiver']