from django.db import models
from django.core.validators import MinValueValidator


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
    )
    calories_value = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
    )

    def __str__(self):
        return f'{self.name} {self.calories_value} kcal'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
