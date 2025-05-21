from rest_framework import serializers

from .models import Usuario, Desempenho, Plano, Treino, Avaliacao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class DesempenhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desempenho
        fields = '__all__'


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = '__all__'


class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
