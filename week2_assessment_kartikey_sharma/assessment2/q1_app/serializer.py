from rest_framework import serializers
from .models import Product
from q1_app.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'