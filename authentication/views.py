from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

# ----- User ---- #

class CreateUserView(CreateAPIView):
    """ Контроллер-класс для регистрации(создания) пользователя """
    queryset = User
    serializer_class = UserSerializer


class LogoutUserView(APIView):
    """ Контроллер-класс для выхода пользователя (logout) """

    def post(self, request):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)
