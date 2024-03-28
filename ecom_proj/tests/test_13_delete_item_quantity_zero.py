from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from cart_app.models import Cart_item
import json


"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

The client will send a series of POST requests to the endpoint with the name of "an_item" to build
the clients cart. 

The client will send a PUT request to the endpoint with the name of "cart_item_quantity"
and pass in "sub" as the method and the number 3 as the cart_item_id to decrement the quantity 
of the Cart_item with the ID of 3 to 0 which will trigger the Cart_Items deletion. 

The client will send a GET request to the endpoint with the name of "cart" to see their updated cart items 
and price.
This endpoint must return the following Response status code of 200
"""
answer = {
    "cart_items": [
        {
            "id": 1,
            "item": {
                "id": 10,
                "category": "Other",
                "name": "Wireless Keyboard and Mouse",
                "price": "20.03",
            },
            "quantity": 1,
        },
        {
            "id": 2,
            "item": {
                "id": 9,
                "category": "Other",
                "name": "Code Editor Subscription",
                "price": "50.10",
            },
            "quantity": 1,
        },
        {
            "id": 4,
            "item": {
                "id": 5,
                "category": "Books",
                "name": "Cracking the Coding Interview",
                "price": "30.27",
            },
            "quantity": 1,
        },
    ],
    "total_price": 100.4,
}
"""
in order to pass the test. Pay attention to order and formatting of your data.
"""


class Test_delete_item_quantity_zero(APITestCase):
    fixtures = ["items.json"]

    def test_013_delete_item_quantity_zero(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        self.client.post(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[9]))
        self.client.post(reverse("an_item", args=[3]))
        self.client.post(reverse("an_item", args=[5]))
        self.client.put(reverse("cart_item_quantity", args=["sub", 3]))
        response = self.client.get(reverse("cart"))
        # print(response.content)
        with self.subTest():
            self.assertTrue(response.status_code==200 and len(Cart_item.objects.all()) == 3)
        self.assertEqual(json.loads(response.content), answer)
