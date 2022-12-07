from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)