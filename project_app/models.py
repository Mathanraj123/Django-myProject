from django.db import models

# Create your models here.
class table3(models.Model):
    name=models.CharField(max_length=50)
    mobno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
class meta:
    db_table=table3