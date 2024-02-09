from django.db import models

# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    scprinc=models.CharField(max_length=100)
    scloc=models.CharField(max_length=100)

    def __str__(self):
        return self.scname
    

class Students(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')


