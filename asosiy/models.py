from django.db import models
from django.utils import timezone
# Create your models here.

class SayohatJoylar(models.Model):
    nomi = models.CharField(max_length = 100)
    qisqa_tarif = models.CharField(max_length=200)
    narx = models.IntegerField()
    rasm = models.ImageField(upload_to = 'rasmlar/sayohat_joylari_rasm')
    
    class Meta:
        verbose_name_plural = "Sayohat Joylari"

    def __str__(self):
        return self.nomi

class Murojat(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length = 17)
    mavzu = models.CharField(max_length = 100)
    xabar = models.TextField()
    sana = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.ism + " || " + self.tel
    

class FoyRoyxat(models.Model):
    ismi=models.CharField(max_length=100)
    email = models.EmailField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ismi + ' || ' + self.email