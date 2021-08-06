from django.db import models

# Create your models here.

class ArtistLabel(models.Model):
    name = models.CharField(max_length=30)
    labeled = models.BooleanField()
    picture = models.ImageField()
    text = models.TextField(max_length=5000)