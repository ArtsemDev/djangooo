from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import BaseAuthentication

from .serializers import ApiRegisterSerializer
from .utils import verify_jwt, create_jwt


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        if not (payload := verify_jwt(token=request.headers.get("Authorization", ""))):
            raise AuthenticationFailed("invalid token")
        # получить пользователя из БД по ID взятому из payload в ключе sub
        #  и вернуть его вместо строки user
        return "user", request.headers.get("Authorization")


class RegistrationApiView(ViewSet):
    serializer = ApiRegisterSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(data=e.detail, status=422)
        token = create_jwt(payload=serializer.data.get("password"))
        return Response(data={"token": token})


class CustomViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        # some logica
        return Response(data={"detail": "OK"}, status=200)
