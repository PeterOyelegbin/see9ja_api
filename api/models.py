from django.db import models

# Create your models here.
class History(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sea9ja/tourism/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Tradition(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sea9ja/traditions/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Art(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='sea9ja/artNculture/')

    def __str__(self):
        return self.title
