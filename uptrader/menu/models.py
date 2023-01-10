from django.db import models
from django.urls import reverse


class Head(models.Model):

    name = models.CharField(max_length=50, unique=True)


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('name', args=[str(self.id)])
    

class Child(models.Model):

    name = models.CharField(max_length=50,)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name