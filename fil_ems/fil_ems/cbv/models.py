from django.db import models
class Product(models.Model):
    prod_id = models.IntegerField(unique=True)
    prod_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()

# Create your models here.
def __str__(self):
    return f"{self.prod_id} {self.prod_name} {self.quantity} {self.price}"