from django.shortcuts import render
from .models import Item
from cart_app.models import Cart_item, Cart
from user_app.models import Client
from .serializers import Item_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

# Create your views here.
class All_items(APIView):
    def get(self, request):
        all_items = Item.objects.all()
        all_items_ser = Item_Serializer(all_items, many=True)
        return Response(all_items_ser.data, status=HTTP_200_OK)


class An_item(APIView):
    def get(self, request, item_id):
        item = Item.objects.get(id=item_id)
        item_ser = Item_Serializer(item)
        return Response(item_ser.data, status=HTTP_200_OK)
    
    def post(self, request, item_id):
        new_cart_item = get_object_or_404(Item, id=item_id)
        user_cart = request.user.cart
        cart_item = Cart_item(cart=user_cart, item=new_cart_item)
        cart_item.full_clean()
        cart_item.save()
        return Response(f"{new_cart_item.name} has been added to your cart", status=HTTP_201_CREATED)
    
    def delete(self, request, item_id):
        item = get_object_or_404(Cart_item, item=item_id)
        item.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Item_by_category(APIView):
    def get(self, request, category):
        items = Item.objects.filter(category=category.title())
        items_ser = Item_Serializer(items, many=True)
        return Response(items_ser.data, status=HTTP_200_OK)