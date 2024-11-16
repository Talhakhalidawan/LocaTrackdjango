from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Attendance(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.CharField(max_length = 100)
    location = models.CharField(max_length = 200)
    # Django Auto datetime
    time_created = models.DateTimeField(auto_now_add = True)
    time_updated = models.DateTimeField(auto_now = True)