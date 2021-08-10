from os import name
from django.db import models
from django.utils import timezone

# Create your models here.

####### Label #######

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


####### BTM #######

class ProdType(models.Model):
    name = models.CharField(max_length=30, verbose_name="Type")
    exemple = models.FileField(verbose_name="Instrumentale exemple", default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Genre de Production'
        verbose_name_plural = 'Genres de Production'

class Prodbeat(models.Model):
    name = models.CharField(max_length=30, verbose_name="Titre")
    reference = models.CharField(max_length=30, verbose_name="Référence")
    music = models.FileField(verbose_name="Musique")
    genre = models.ForeignKey(ProdType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Production'
        verbose_name_plural = 'Productions'


####### LD2J #######
class LD2JContributor(models.Model):
    name = models.CharField(verbose_name="Nom de scène du contributeur", max_length=30)
        
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Contributeur'
        verbose_name_plural = 'Contributeurs'

class LD2JMusic(models.Model):
    name = models.CharField(verbose_name="Titre", max_length=30)
    contributors = models.ManyToManyField(LD2JContributor, verbose_name="Contributeurs", blank=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Musique'
        verbose_name_plural = 'Musiques'


class DateWithoutTZField(models.DateField):
    def db_type(self, connection):
        return 'date'

class LD2JAlbum(models.Model):
    name = models.CharField(verbose_name="Titre de l'album", max_length=30)
    released = DateWithoutTZField(verbose_name="Date de sortie")
    picture = models.ImageField(verbose_name="Jaquette")
    contributors = models.ManyToManyField(LD2JContributor, verbose_name="Contributeurs", blank=True)
    hyperfollowlink = models.URLField(verbose_name="Lien Hyperfollow")
    musics = models.ManyToManyField(LD2JMusic, verbose_name="Musiques")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
