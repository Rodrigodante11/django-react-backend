from django.shortcuts import render
from .serializers import ListaSerializer
from rest_framework import viewsets, permissions
from .models import Lista


class ListViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [permissions.IsAuthenticated] # acesso a pessoa autenticada
