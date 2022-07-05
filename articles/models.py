from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    content = models.TextField()
