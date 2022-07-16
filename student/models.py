from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name
