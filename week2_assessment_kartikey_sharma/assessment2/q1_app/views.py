from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retreive(self, request, pk=None):
        if pk is not None:
            customer = Product.objects.get(id=pk)
            serializer =ProductSerializer(customer)
            return Response(serializer.data)
        
    def update(self, request, pk=None):
        if pk is not None:
            customer = Product.objects.get(id=pk)
            serializer = ProductSerializer(Product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def destroy(self, request, pk=None):
        if pk is not None:
            customer = Product.objects.get(id=pk)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)      
        

# Create your views here.
