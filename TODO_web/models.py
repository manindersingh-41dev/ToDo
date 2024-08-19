from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class consumers(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return self.username
    
class Todo(models.Model):
    consumer = models.ForeignKey(consumers, null=True,on_delete=models.SET_NULL)
    task = models.CharField(max_length=9999999999999999999999999999)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task