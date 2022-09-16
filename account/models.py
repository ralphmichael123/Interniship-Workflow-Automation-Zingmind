from django.db import models

# Create your models here.
class account(models.Model):
    ID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    Email = models.EmailField(max_length=70)
    Password=models.CharField(max_length=70)
    Contact_number= models.CharField(max_length=70)
    address= models.CharField(max_length=70)


class request(models.Model):
    request_type = models.CharField(max_length=70)
    date = models.CharField(max_length=70)
    approve_name = models.CharField(max_length=70)
    request_time = models.CharField(max_length=70)
