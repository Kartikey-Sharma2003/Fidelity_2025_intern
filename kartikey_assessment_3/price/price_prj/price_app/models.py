from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True, null=True, blank=True)
    customer_phone = models.CharField(max_length=15)

    def _str_(self):
        return self.name