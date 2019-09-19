from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers

users = [
    {'nome': 'Rodrigo Araújo', 'nascimento': '10/07/1985'},
    {'nome': 'Emanuel Gomes', 'nascimento': '12/09/2001'}
]


class ListUsers(APIView):

    def get(self, request, format=None):
        return Response(users)


class CreateNewUser(APIView):

    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            users.append(user)
        return Response()
