from django.db import models

# Create your models here.

class client(models.Model):
    
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    phone_number = models.CharField( max_length=50)
    Duedate= models.DateField(null=True)
