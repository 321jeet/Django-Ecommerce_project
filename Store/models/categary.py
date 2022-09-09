
from django.db import models

class Categary(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
       return self.name
   


    @staticmethod
    def get_all_categary():
       return Categary.objects.all()



