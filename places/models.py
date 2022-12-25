from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Place(models.Model):
    """Place Model"""
    name = models.CharField(verbose_name="Название", max_length=100)
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    rating = models.IntegerField(verbose_name="Рейтинг",
                                 validators=[
                                     MaxValueValidator(25),
                                     MinValueValidator(0)
                                 ])

    class Meta:
        verbose_name = "Примечательное место"
        verbose_name_plural = "Примечательные места"

    def __str__(self):
        return self.name
