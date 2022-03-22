from django.db import models

# Create your models here.

class Team(models.Model):
    photo = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, null=True)
    address  = models.TextField()
    mobile = models.IntegerField()
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    pics = models.ImageField(upload_to="images/")
    
class Msg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()