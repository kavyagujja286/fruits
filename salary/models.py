from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    scientific_name=models.CharField(max_length=100)
    use=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    season=models.CharField(max_length=10)
    cost=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.name
    

    