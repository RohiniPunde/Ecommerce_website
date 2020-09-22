from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length= 100)
    description=models.TextField()
    image=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Order(models.Model):
    items=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    total=models.CharField(max_length=100)

    def __str__(self):
        return self.name
