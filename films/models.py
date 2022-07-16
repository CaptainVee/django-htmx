from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


class Film(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    content = models.TextField(default="This is a nice movie")
    date_posted = models.DateTimeField(default=timezone.now)
    order = models.IntegerField(default=1)

    # class Meta:
    #     ordering = ['name']
