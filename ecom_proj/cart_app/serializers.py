from rest_framework import serializers
from .models import Cart_item
from item_app.serializers import Item_Serializer

class Cart_Item_Serializer(serializers.ModelSerializer):
    item = Item_Serializer()
    
    class Meta:
        model = Cart_item
        fields = ["id", "item", "quantity"]