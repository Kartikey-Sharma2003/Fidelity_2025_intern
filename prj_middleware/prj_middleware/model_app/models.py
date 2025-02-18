from django.db import models
class Manager(models.Model):
    m_id = models.IntegerField(unique=True)
    m_fname=models.CharField(max_length=100)
    m_laels.CharField(max_length=100)
    salary = models.IntegerField()
    doj = models.DateField()
    manages = models.IntegerField()


    def __str__(self):
        return f"{self.m_fname} {self.m_lname} {self.salary} {self.doj}"

class commonInfo(models.Model):
    name = models.CharField(max_length=100)
    fame = models.CharField(max_length=100)
    salary = models.IntegerField()
    doj = models.DateField()
    e_id = models.IntegerField(unique=True)
