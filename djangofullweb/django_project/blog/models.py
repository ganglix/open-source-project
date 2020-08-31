from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here. to be saved to the data base

class Post(models.Model):  # inheriate 
    title = models.CharField(max_length=100)
    content = models.TextField()  # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # user to post, one to many, if the user is deleted the model is deleted, not the way around

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})  # and view will handle redirect
    