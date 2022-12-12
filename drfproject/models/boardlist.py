from django.db import models

class BoardList(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
