from .models import Lista
from rest_framework import serializers


class ListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lista
        fields = ['owner', 'name', 'url']
