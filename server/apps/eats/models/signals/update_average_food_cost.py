from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

from apps.eats.models import Dish, Institution


@receiver(post_save, sender=Dish)
def update_average_food_cost(sender, instance, created, **kwargs):
    institution = instance.institution
    institution.average_food_cost = institution.dish_set.aggregate(avg=Avg('price'))['avg']
    institution.save()
