from turtle import title
from django.db import models
from django.contrib.auth.models import get_user_models
from datetime import datetime
from time import timezone

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=200)
    Author = models.ForeignKey(get_user_models(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateTimeField(auto_now=True)