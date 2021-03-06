from django.db import models

from datetime import datetime, date

class Item(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)

class auction_table(models.Model):
    owner_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    timestamp =  models.DateTimeField(default=datetime.now, blank=True)