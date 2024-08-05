# from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Client
from cart_app.models import Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class Sign_Up(APIView):
    def post(self, request):
        request.data["username"] = request.data.get("email")
        user = Client.objects.create_user(**request.data)
        token = Token.objects.create(user=user)
        cart = Cart(client=user)
        cart.full_clean()
        cart.save()
        return Response({"client": user.email, "token": token.key}, status = HTTP_201_CREATED)
        

class Log_in(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "client": user.email}, status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})

class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)