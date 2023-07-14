from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
