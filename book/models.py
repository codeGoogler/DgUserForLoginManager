# coding:utf-8
from django.db import models

# Create your models here.

class Book(models.Model):
    btitle = models.CharField(max_length=10)
    bpub_date = models.DateTimeField()

class Hero(models.Model):
    htitle = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('Book','on_delete=models.CASCADE()')


