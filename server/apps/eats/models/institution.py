from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from yandex_geocoder import Client


class Institution(models.Model):
    name = models.CharField(
        max_length=255,
    )
    address = models.CharField(
        max_length=500,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
    )
    working_hours_begin = models.TimeField()
    working_hours_end = models.TimeField()
    average_food_cost = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        editable=False,
        default=0,
    )
    latitude = models.FloatField(
        editable=False,
    )
    longitude = models.FloatField(
        editable=False,
    )

    def __str__(self):
        return self.name

    def get_coordinates(self):
        """
        Get coordinates from Yandex API by string representation of the address.
        Api key is stored in the docker env variables.
        """
        api_key = settings.YANDEX_API_KEY
        client = Client(api_key)
        coordinates = client.coordinates(self.address)
        return coordinates[0], coordinates[1]

    def save(self, *args, **kwargs):
        """
        An overriden method from the base class sets 'readonly' variables.
        """
        self.latitude, self.longitude = self.get_coordinates()
        super(Institution, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'
