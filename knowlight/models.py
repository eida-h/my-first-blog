from django.db import models

# Create your models here.

class knowPost(models.Model):
    station = models.TextField()
    text = models.TextField()