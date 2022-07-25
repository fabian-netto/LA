from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=20)
    brief = models.CharField(max_length=200)
    img = models.ImageField()

    def __str__(self):
        return self.name  
