from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import Sum

from apps.eats.models import Dish


@receiver(m2m_changed, sender=Dish.ingredients.through)
def update_calories_value(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    if kwargs['pk_set']:
        ingredient_set = kwargs['model'].objects.filter(id__in=kwargs['pk_set'])
        instance.calories_value = ingredient_set.aggregate(sum=Sum('calories_value'))['sum']
    instance.save()
