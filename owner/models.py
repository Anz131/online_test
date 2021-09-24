from django.db import models

# Create your models here.

class Test(models.Model):
    question=models.CharField(max_length=500,unique=True)
    a=models.CharField(max_length=50,null=True)
    b=models.CharField(max_length=50,null=True)
    c=models.CharField(max_length=50,null=True)
    d=models.CharField(max_length=50,null=True)


    def __str__(self):
        return  self.question