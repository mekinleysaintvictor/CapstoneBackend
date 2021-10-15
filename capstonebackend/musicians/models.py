from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
from autoslug import AutoSlugField

# Create your models here.
class Musician(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        aboutMe = models.CharField(max_length=500, default='None')
        instruments = models.CharField(max_length=100, default='None')
        influences = models.CharField(max_length=100, default='None')
        genres = models.CharField(max_length=100, default='None')
        # slug = AutoSlugField(populate_from='user', default='None')
        friends = models.ManyToManyField("Musician", blank=True)

        def __str__(self):
            return str(self.user.username)

        # def get_absolute_url(self):
        #     return "/users/{}".format(self.slug)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Musician.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

#BandRequests
class FriendRequest(models.Model):
        to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
        from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return "From {}, to {}".format(self.from_user.username, self.to_user.username)


    # video = models.CharField(max_length=500)
    # jam = models.IntegerField()
    # profilePic = models.ImageField()
    #influences/fk, band/fk
    #influences - artist, genre, band pic
    #band - bandname, members, bandSInce