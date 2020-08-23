from rest_framework.serializers import ModelSerializer

from apps.eats.models import Institution


class InstitutionSerializer(ModelSerializer):

    class Meta:
        model = Institution
        fields = (
            'name',
            'address',
            'owner',
            'image',
            'working_hours_begin',
            'working_hours_end',
            'average_food_cost',
            'latitude',
            'longitude',
        )

    def create(self, validated_data):
        validated_data['owner'] = self.context.get('request').user
        institution = Institution.objects.create(**validated_data)
        return institution
