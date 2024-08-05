from django.db import models

# Create your models here.
class Item(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255, null=False, blank=False)
    # one to one relationship connecting cart item to this primary key

    def add_to_cart(self):
        self.cart_item.add(0)