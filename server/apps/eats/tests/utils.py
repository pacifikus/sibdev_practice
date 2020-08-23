from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


def create_user(username, email, password):
    user = User.objects.create(
        username=username,
        email=email,
    )
    user.set_password(password)
    user.save()
    token = Token.objects.get_or_create(user=user)
    return user, token
