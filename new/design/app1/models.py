from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.TextField(max_length=50)
    desc=models.TextField(max_length=200)
    image=models.ImageField(upload_to="design/cover",null=True,blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.TextField(max_length=30)
    desc=models.TextField(max_length=200)
    image=models.ImageField(upload_to="design/teams",null=True,blank=True)

    def __str__(self):
        return self.name

