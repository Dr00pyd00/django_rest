
from django.db import models

from django.conf import settings 

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

    @property
    def is_available(self):
        # si dans ces loans , une return date est null ca veut dire quil est en cours d'emprunt,
        # donc on return l'inverse donc False
        return not self.loan_set.filter(return_date__isnull=True).exists()

    def __str__(self):
        return self.title


class Loan(models.Model):   # emprunt
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    loan_date = models.DateField(auto_now_add=True)    # rempli automaitquement la date actuelle a la creation de l'objet
    return_date = models.DateField(null=True,blank=True)     # si null : livre NON dispo / si notnull : livre dispo

    def __str__(self):
        return f'loan {self.book} by {self.user}'




