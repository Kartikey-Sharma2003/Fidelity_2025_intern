from django.shortcuts import render
from rest_framework import viewsets
from viewset_app.models import Customer
from viewset_app.serializer import CustomerSerializer
from rest_framework.response import Response

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    
    def retreive(self, request, pk=None):
        if pk is not None:
            customer = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=201)
        return Response(serializer.errors, status=400)
    def update(self, request, pk=None):
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return Response({'msg': 'Data Deleted'})    


# Create your views here.
