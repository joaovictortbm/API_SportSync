# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Desempenho, Plano, Treino, Avaliacao
from .serializers import UsuarioSerializer, DesempenhoSerializer, PlanoSerializer, TreinoSerializer, AvaliacaoSerializer

# Mapeamento dos modelos e serializers
MODEL_MAP = {
    'usuario': (Usuario, UsuarioSerializer),
    'desempenho': (Desempenho, DesempenhoSerializer),
    'plano': (Plano, PlanoSerializer),
    'treino': (Treino, TreinoSerializer),
    'avaliacao': (Avaliacao, AvaliacaoSerializer),
}

# Método para listar todos os objetos de um model


@api_view(['GET'])
def list_objects(request, model_name):
    # Verifica se o modelo existe no mapeamento
    if model_name not in MODEL_MAP:
        return Response({'error': 'Modelo inválido'}, status=status.HTTP_400_BAD_REQUEST)
    model, serializer_class = MODEL_MAP[model_name]
    objs = model.objects.all()
    serializer = serializer_class(objs, many=True)
    return Response(serializer.data)

# Método para recuperar um objeto específico pelo ID


@api_view(['GET'])
def list_object_byID(request, model_name, pk):
    if model_name not in MODEL_MAP:
        return Response({'error': 'Modelo inválido'}, status=status.HTTP_400_BAD_REQUEST)
    model, serializer_class = MODEL_MAP[model_name]
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_class(obj)
    return Response(serializer.data)

# Método para criar um objeto


@api_view(['GET', 'POST'])
def create_object(request, model_name):
    if model_name not in MODEL_MAP:
        return Response({'error': 'Modelo inválido'}, status=status.HTTP_400_BAD_REQUEST)
    model, serializer_class = MODEL_MAP[model_name]
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Método para atualizar um objeto


@api_view(['GET', 'PUT'])
def update_object(request, model_name, pk):
    if model_name not in MODEL_MAP:
        return Response({'error': 'Modelo inválido'}, status=status.HTTP_400_BAD_REQUEST)
    model, serializer_class = MODEL_MAP[model_name]
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_class(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Método para deletar um objeto
@api_view(['GET', 'DELETE'])
def delete_object(request, model_name, pk):
    if model_name not in MODEL_MAP:
        return Response({'error': 'Modelo inválido'}, status=status.HTTP_400_BAD_REQUEST)
    model, serializer_class = MODEL_MAP[model_name]
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    obj.delete()
    return Response({'message': 'Objeto deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
