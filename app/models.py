from django.db import models

# Create your models here.


class Items(models.Model):
    task=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.task
    