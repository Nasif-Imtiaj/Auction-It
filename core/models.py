from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
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
    description = models.TextField(default="none")
    image = models.ImageField(default="default_cat", upload_to='Category_pics')

    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=50)
    timestamp =  models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class AuctionItem(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    is_sold = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField()


    def get_absolutre_url(self):
        return reverse('', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

class Images(models.Model):
    item = models.ForeignKey(AuctionItem,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='auction_item_pics')

    def __str__(self):
        return self.item.name + " Img"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Bets(models.Model):
    item = models.ForeignKey(AuctionItem,on_delete=models.CASCADE)
    better = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_accepted = models.BooleanField(default=False)
    betted_time = models.DateTimeField(default=timezone.now)
    accepted_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('item', 'better')
        verbose_name = 'Bet'
        verbose_name_plural = 'Bets'


"""
items = self.request.user.auction_item_set.all()
Bets.objects.filter(item__in=items, is_accepted=True)
Bets.objects.filter(item=self.request.user, is_accepted=True)
self.request.user.bets_set.filter(is_accepted=True)
"""