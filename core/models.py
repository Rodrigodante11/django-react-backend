from django.db import models
from django.contrib.auth.models import User


class Lista(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    list = models.ForeignKey(Lista, on_delete=models.CASCADE)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.name


