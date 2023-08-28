from django.db import models

# Create your models here.
class weather:
    weather = models.CharField(verbose_name="Weather")
    city = models.CharField(verbose_name="City")
    date = models.DateField(verbose_name="Date")
    def __str__(self) -> str:
        return self.weather