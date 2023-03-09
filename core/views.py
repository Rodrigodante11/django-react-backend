from django.shortcuts import render
from .serializers import ListaSerializer, ItemSerializer
from rest_framework import viewsets, permissions, authentication
from .models import Lista, Item


class ListViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [permissions.IsAuthenticated]  # acesso a pessoa autenticada
    authentication_classes = [authentication.TokenAuthentication]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated] # acesso a pessoa autenticada
    authentication_classes = [authentication.TokenAuthentication]
