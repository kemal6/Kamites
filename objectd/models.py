from django.db import models

# Create your models here.

class Object(models.Model):
    Nom = models.CharField(max_length=510)
    Description = models.TextField()
    Ethnie= models.CharField(max_length=510)
    Pays = models.CharField(max_length=510)
    Materiaux = models.CharField(max_length=510)
    Hauteur_cm = models.CharField(max_length=510)
    Largeur_cm = models.CharField(max_length=510)
    Poids = models.CharField(max_length=510)
    Datation = models.CharField(max_length=510)
    img= models.CharField(max_length=510)
    img1= models.CharField(max_length=510)
    img2= models.CharField(max_length=510)
    img3= models.CharField(max_length=510)
    img4= models.CharField(max_length=510)
    img5= models.CharField(max_length=510)
    img6= models.CharField(max_length=510)
    img7= models.CharField(max_length=510)
    img8= models.CharField(max_length=510)
    img9= models.CharField(max_length=510)
    img10= models.CharField(max_length=510)
    img11= models.CharField(max_length=510)
    img12= models.CharField(max_length=510)

    def __str(self):
        return self.Nom
