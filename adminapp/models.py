from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class aktualniden(models.Model):
    cislo_dne = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)])

    def __str__(self):
        return f'den č:{self.cislo_dne}'
    

class food_drink(models.Model):
    food_img = models.ImageField(upload_to='food_images/')
    food_name = models.CharField()
    food_znacka = models.CharField()
    food_typ = models.CharField()
    food_vaha = models.FloatField(default=0)
    food_objem = models.FloatField(default=0)
    food_kcal = models.FloatField(default=0)
    food_sytost = models.FloatField(default=0)
    food_hydratace = models.FloatField(default=0)
    food_bonus_typ = models.CharField()
    food_bonus_hodnota = models.FloatField(default=0)
    food_cena = models.FloatField(default=0)
    food_pozn = models.CharField()

    def __str__(self):
        return f'{self.food_typ} - {self.food_name}'