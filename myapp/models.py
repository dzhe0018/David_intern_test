from django.db import models

# Create your models here.
from django.db import models

class Entry(models.Model):
    #Create a model contains name(max 70) and age
    name = models.CharField(max_length=70)
    age = models.IntegerField()


    def __str__(self):
        return self.name

