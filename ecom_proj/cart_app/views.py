from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cart, Cart_item
from .serializers import Cart_Item_Serializer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

# Create your views here.

class Cart_manager(APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = request.user.cart.cart_items
        cart_items_ser = Cart_Item_Serializer(cart_items, many=True)

        total_price = 0
        for item in cart_items_ser.data:
            total_price += float(item.get("item").get("price")) * item.get("quantity")
        total_price = round(total_price, 2)

        return Response({"cart_items": cart_items_ser.data, "total_price": total_price}, status=HTTP_200_OK)
    
class Cart_Item_Quantity(APIView):
    def put(self, request, method, cart_item_id):
        cart_item = request.user.cart.cart_items.get(id=cart_item_id)

        if method == "add":
            cart_item.quantity += 1
            cart_item.save()
            return Response(status=HTTP_200_OK)
        elif method == "sub":
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
        

class Delete_Item(APIView):
    def delete(self, request, cart_item_id):
        cart_item = request.user.cart.cart_items.get(id=cart_item_id)
        cart_item.delete()
        
        return Response(HTTP_200_OK)