from django.db import models
from apps.eats.models import Ingredient, Institution
from django.core.validators import MinValueValidator


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
    )
    image = models.ImageField(
        upload_to='images/dishes/',
        blank=True,
    )
    calories_value = models.IntegerField(
        editable=False,
        default=0,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
    )
    ingredients = models.ManyToManyField(Ingredient)
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
