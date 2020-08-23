from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def get_token(self, user_instance):
        token = Token.objects.get(user=user_instance).key
        return token

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        Token.objects.create(user=user)
        return user
