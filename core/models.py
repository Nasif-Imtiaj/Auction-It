from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
class Item(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)

class auction_table(models.Model):
    owner_name = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    timestamp =  models.DateTimeField(default=datetime.now, blank=True)

    def get_absolutre_url(self):
        return reverse('', kwargs={'pk': self.pk})

class Category(models.Model):
    title = models.CharField(max_length=50)
    timestamp =  models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class AuctionItem(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

