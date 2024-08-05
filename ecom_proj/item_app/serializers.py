from rest_framework import serializers
from .models import Item

class Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "category", "name", "price"]