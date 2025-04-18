from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AddBook(models.Model):
    title = models.CharField(max_length=255,default='Unknown Title')
    author = models.CharField(max_length=255,default='Unknown Author')

    def __str__(self):
        return self.title