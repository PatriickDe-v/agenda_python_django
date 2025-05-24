from django.db import models

# Create your models here.
 
#Essa classe herda do models do Model
class Contact(models.Model):
    first_name = models.CharField(max_length=50);