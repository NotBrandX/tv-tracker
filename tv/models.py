from django.db import models

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    network = models.TextField()

    def __str__(self):
        return self.name