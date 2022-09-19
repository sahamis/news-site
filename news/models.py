from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    published_date=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
