from django.db import models

# Create your models here.
class pokemon(models.Model):
    pokename= models.CharField(max_length=100)
    def __str__(self):
        return self.pokename