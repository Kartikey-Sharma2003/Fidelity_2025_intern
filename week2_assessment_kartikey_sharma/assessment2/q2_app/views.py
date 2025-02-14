from django.shortcuts import render
from rest_framework import viewsets
from .models import QuestionPaper
from .serializer import QuestionPaperSerializer
from rest_framework.response import Response
from rest_framework import status

class QuestionPaper(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionPaperSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = QuestionPaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retreive(self, request, pk=None):
        if pk is not None:
            customer = QuestionPaper.objects.get(id=pk)
            serializer =QuestionPaperSerializer(customer)
            return Response(serializer.data)
        
    def update(self, request, pk=None):
        if pk is not None:
            customer = QuestionPaper.objects.get(id=pk)
            serializer = QuestionPaperSerializer(QuestionPaper, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def destroy(self, request, pk=None):
        if pk is not None:
            customer = QuestionPaper.objects.get(id=pk)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
