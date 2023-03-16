from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactForm(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    contacted_status = models.BooleanField(default=False)
    

class CallBackForm(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    time = models.DateTimeField()
    query = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    contacted_status = models.BooleanField(default=False)
    
class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)