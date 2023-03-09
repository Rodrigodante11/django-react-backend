from .models import Lista
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'list', 'comprado', 'url']


class ListaSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = Lista
        fields = ['owner', 'name', 'item_set' , 'url']



