from django.db import models
class Liste(models.Model):
    destination=models.CharField(max_length=100)
    compagnie=models.CharField(max_length=100)
    prixTicket=models.FloatField()
    numVol=models.IntegerField()
    dateDepart=models.DateField()
    air=models.ForeignKey('Aeroport',on_delete=models.CASCADE,)
    def __str__(self) -> str:
            return self.destination

class Aeroport(models.Model):
    nomAir=models.CharField(max_length=20)
    description=models.TextField()
    def __str__(self) -> str:
            return self.nomAir