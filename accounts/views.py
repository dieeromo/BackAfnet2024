from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import UserAccount
from .serializers import UserCreateSerializer, usuario_serializador_creado

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listUserAccount(request):
    usuarios = UserAccount.objects.filter().order_by('id')
    #serializer = UserCreateSerializer(usuarios, many=True)
    serializer = usuario_serializador_creado(usuarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listDocentes(request):
    usuarios = UserAccount.objects.filter(is_docente = True).order_by('id')
    #serializer = UserCreateSerializer(usuarios, many=True)
    serializer = usuario_serializador_creado(usuarios, many=True)
    return Response(serializer.data)
