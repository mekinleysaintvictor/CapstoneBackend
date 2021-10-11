from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aboutMe = models.CharField(max_length=500, default='None')
    instruments = models.CharField(max_length=100, default='None')
    influences = models.CharField(max_length=100, default='None')
    genres = models.CharField(max_length=100, default='None')
    # video = models.CharField(max_length=500)
    # jam = models.IntegerField()
    # profilePic = models.ImageField()
    #influences/fk, band/fk
    #influences - artist, genre, band pic
    #band - bandname, members, bandSInce