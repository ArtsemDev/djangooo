from collections import OrderedDict
from re import fullmatch

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework.fields import EmailField, CharField


class ApiRegisterSerializer(Serializer):
    email = EmailField()
    password = CharField(min_length=8)
    password2 = CharField(min_length=8)

    def validate(self, attrs: OrderedDict):
        if attrs.get("password") != attrs.get("password2"):
            raise ValidationError(detail="password does not match with password2")

        if fullmatch(
                pattern=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                string=attrs.get("password")
        ) is None:
            raise ValidationError(detail="password simple")

        return attrs

