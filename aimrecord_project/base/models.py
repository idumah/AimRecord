from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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





# Create your models here.
