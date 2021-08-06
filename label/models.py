from django.db import models

# Create your models here.

class ArtistLabel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nom d'artiste")
    labeled = models.BooleanField(verbose_name="A fait parti du label ?")
    picture = models.ImageField(verbose_name="Image")
    text = models.TextField(max_length=5000, verbose_name="Texte de présentation")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Artiste Client/Labelisé'
        verbose_name_plural = 'Artistes Clients/Labelisés'