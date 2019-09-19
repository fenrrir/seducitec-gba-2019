from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    nome = serializers.CharField()
    nascimento = serializers.DateField(input_formats=['%d/%M/%y'])

    def create(self, validated_data):
        return {'nome': validated_data['nome'], 'nascimento': validated_data['nascimento']}