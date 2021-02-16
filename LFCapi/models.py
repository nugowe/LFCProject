from django.db import models

class LFCStrikers(models.Model):
    PlayerName = models.CharField(max_length=100)
    JerseyNumber = models.CharField(max_length=100)

def __str__(self):
    return self.title

    
class LFCDefenders(models.Model):
    PlayerName = models.CharField(max_length=100)
    JerseyNumber = models.CharField(max_length=100)

def __str__(self):
    return self.title

# Create your models here.
