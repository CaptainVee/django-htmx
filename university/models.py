from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modeules')

    def __str__(self):
        return self.name
