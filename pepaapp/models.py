from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models import Avg, Sum

#SELECT * FROM pepaapp_Hracipepa; <-- Query příkaz v querytool

class Hracipepa(models.Model):
    jmeno = models.CharField(max_length=20)
    prijmeni = models.CharField(max_length=30)
    tym = models.CharField(max_length=10, null=True) #pepa/karel/brunhilda
    kroky1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky11 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    kroky12 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50000)])
    celkem_kroku = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000000)])


#formát zobrazení v administraci
    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'
    
    def save(self, *args, **kwargs):
        self.celkem_kroku = (
            (self.kroky1) + (self.kroky2) + (self.kroky3) + (self.kroky4) +
            (self.kroky5) + (self.kroky6) + (self.kroky7) + (self.kroky8) +
            (self.kroky9) + (self.kroky10) + (self.kroky11) + (self.kroky12)
        )
        super().save(*args, **kwargs) # Volání původní metody save()


class pepaspanek(models.Model):
    den = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)])
    spanek = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
    odpocinek = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
    aktivita = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])

    def __str__(self):
        return f'Den č:{self.den}'
    

class pepa_zakladni_staty(models.Model):
    jmeno = models.CharField(max_length=10)
    vek = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    vyska = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    vaha = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)])
    pohlavi = models.CharField(max_length=10)
    delkakroku = models.FloatField(default=0)
    

    def __str__(self):
        return f'{self.jmeno} - ZÁKLADNÍ staty'