from email.mime import image
from django.db import models

# Create your models here.
class Tradition(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to = 'sea9ja/traditions/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title