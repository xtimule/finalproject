from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    def __str__(self):
        return self.name


class Tovar(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField()
    cost = models.IntegerField()
    category = models.ForeignKey(Category, related_name='tovary', on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, default='')
    weight = models.IntegerField()
# Create your models here.