from rest_framework.response import Response
from rest_framework.views import APIView

users = [
    {'nome': 'Rodrigo Araújo', 'nascimento': '10/07/1985'},
    {'nome': 'Emanuel Gomes', 'nascimento': '12/09/2001'}
]


class ListUsers(APIView):

    def get(self, request, format=None):
        return Response(users)


class CreateNewUser(APIView):

    def post(self, request, format=None):
        user = {'nome': request.POST.get('nome'), 'nascimento': request.POST.get('nascimento')}
        users.append(user)
        return Response()
