from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)
