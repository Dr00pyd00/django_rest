
from django.db import models

# Create your models here.
# id est automatique 
# null=True : autorise NULL en base de donnees  (SQL)
# blank=True : autorise null dans les formulaires python

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title




