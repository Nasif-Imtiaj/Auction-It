from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    full_name = models.CharField(default='@Example_name', max_length=100)
    phone_number =  models.TextField(default='@Example_045978346')
    address = models.TextField(default='@Example_13-65 new jersey')
    last_active = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(default='You bio')


    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def update_last_active(self):
        self.last_active = timezone.now()
        self.save()
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

