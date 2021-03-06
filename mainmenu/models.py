from django.db import models
from django.contrib.auth import get_user_model

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
    shtrix = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Card(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    organization = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    comments = models.TextField()
    def __str__(self) -> str:
        return f"{self.user.username}: {self.added_date}"


class CardItem(models.Model):
    product = models.ForeignKey(Tovar, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Card, related_name="carditems", on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.product.name
