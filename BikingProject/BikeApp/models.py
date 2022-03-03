from django.db import models
from login_and_reg_app.models import *

# Create your models here.
class Ride(models.Model):
    ridetitle = models.CharField(max_length=60)
    startingpoint = models.CharField(max_length=100)
    routefile = models.FileField(upload_to='rides/routefiles', max_length=100, default="No file uploaded")
    distance = models.CharField(max_length=10)
    dateofride = models.DateField()
    skill = models.CharField(max_length=60)
    desc = models.TextField()
    ride_start_time = models.CharField(max_length=20)
    est_end_time = models.CharField(max_length=20)
    ride_creator = models.ForeignKey(User, related_name="ridescreated", on_delete=models.CASCADE)
    users_joined = models.ManyToManyField(User, related_name="usersriding")
    rides_joined = models.ManyToManyField(User, related_name="myrides")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)