from django.db import models


# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
