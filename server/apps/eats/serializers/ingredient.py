from rest_framework.serializers import ModelSerializer

from apps.eats.models import Ingredient


class IngredientSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'calories_value', )
