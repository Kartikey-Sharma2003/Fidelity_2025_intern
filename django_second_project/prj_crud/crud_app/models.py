from django.db import models

class Orders(models.Model):
    ordId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    price=models.FloatField()
    email=models.EmailField()
    addr=models.CharField(max_length=100)


# Create your models here.
