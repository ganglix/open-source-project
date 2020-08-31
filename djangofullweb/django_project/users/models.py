from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# one to one 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):  # this save is to overwrite the parent class to add more functionality
        super().save()  # parent method

        img = Image.open(self.image.path)  # open image of the current instance
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # overwrite