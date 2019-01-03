from django.db import models

# Create your models here.

class dong_data(models.Model):
    dong = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    medical = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    house = models.CharField(max_length=100)

    def __str__(self):
        return self.dong