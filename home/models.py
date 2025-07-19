from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Deliver(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    add=models.TextField(max_length=60)
    def __str__(self):
        return self.name
class Menu(models.Model):
    name=models.CharField(max_length=30)
    id=models.CharField(max_length=3,primary_key=True)
    description=models.CharField(max_length=60)
    price=models.FloatField()
    # id.set('primary_key=True')
    def __str__(self):
        return self.name
    

                

 