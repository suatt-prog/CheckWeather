from django.db import models

# Create your models here.
class weather(models.Model):
    weather = models.CharField(verbose_name="Weather", max_length=1000)
    city = models.CharField(verbose_name="City", max_length=50)
    date = models.DateField(verbose_name="Date")
    def __str__(self) -> str:
        return self.weather