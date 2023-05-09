from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=888, null=False,blank= False)
    Email=models.EmailField(max_length=888, null=False,blank= False)
    Phonenumber=models.CharField(max_length=888, null=False,blank= False)
    Mownika=models.CharField(max_length=888, null=False,blank= False)

