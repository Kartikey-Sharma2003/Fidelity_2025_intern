from rest_framework import serializers
from .models import QuestionPaper
from q2_app.models import QuestionPaper

class QuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = '__all__'