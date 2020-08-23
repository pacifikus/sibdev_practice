from rest_framework.serializers import ModelSerializer
from apps.eats.models import Dish


class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = ('name', 'image', 'calories_value', 'price', 'ingredients', 'institution', )
