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
