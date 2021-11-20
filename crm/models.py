from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)