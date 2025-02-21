from django.db import models

# Create your models here.


class School(models.Model):        #table name
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=40)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
