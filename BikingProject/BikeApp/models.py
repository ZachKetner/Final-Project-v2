from django.db import models

# Create your models here.
class Ride(models.Model):
    ridetitle = models.CharField(max_length=60)
    startingpoint = 
    routefile = models.FileField(upload_to=None, max_length=100)
    distance = models.CharField(max_length=10)
    dateofride = models.DateField()
    skill = models.CharField(max_length=60)
    desc = models.TextField()
    ride_start_time = models.CharField(max_length=20)
    est_end_time = models.CharField(max_length=20)
    ride_creator = 
    user_joined = 
    rides_joined =