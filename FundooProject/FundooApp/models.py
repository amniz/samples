from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.
# created_at created_by modified_at modified_by
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=  models.CASCADE)

    age=models.IntegerField()
    def __str__(self):
        return self.user.username



class FundooNotes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    note=models.TextField(max_length=1025)
    reminder=models.DateTimeField()
    collaborator=models.EmailField(max_length=255)
    color=models.CharField(max_length=10)
    image=models.ImageField()
    archieve=models.BooleanField(default=False)

