from django.db import models
from user_app.models import Client
from item_app.models import Item

# Create your models here.
class Cart(models.Model):
    client = models.OneToOneField(Client, related_name="cart", on_delete=models.CASCADE)

class Cart_item(models.Model):
    quantity = models.IntegerField(null=False, blank=False, default=1)
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    item = models.OneToOneField(Item, related_name="cart_item", on_delete=models.CASCADE)