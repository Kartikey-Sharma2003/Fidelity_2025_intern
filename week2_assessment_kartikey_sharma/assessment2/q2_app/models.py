from django.db import models



class QuestionPaper(models.Model):
    q_no = models.IntegerField(primary_key=True)
    q_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.q_name
    

# Create your models here.
