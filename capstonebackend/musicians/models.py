from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aboutMe = models.CharField(max_length=500)
    video = models.CharField(max_length=500)
    profilePic = models.ImageField()
    jam = models.IntegerField()
    #influences/fk, band/fk
    #influences - artist, genre, band pic
    #band - bandname, members, bandSInce
    def __str__(self):
        return self.name