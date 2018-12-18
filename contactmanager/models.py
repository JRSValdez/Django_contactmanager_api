from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.name
