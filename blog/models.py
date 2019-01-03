from django.db import models
from django.utils import timezone

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, default=1)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.titre

