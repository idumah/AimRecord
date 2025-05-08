from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

class Participant(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    bow_type = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    club = models.CharField(max_length=100)

class Butt(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    number = models.IntegerField()

class Target(models.Model):
    butt = models.ForeignKey(Butt, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    letter = models.CharField(max_length=2)





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    # Добавьте любые другие поля

    def __str__(self):
        return f'{self.user.username} Profile'


# Сигналы для автоматического создания профиля
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# Create your models here.
