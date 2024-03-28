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

The client will then send a mix of POST and DELETE requests to the endpoint of "an_item" 
to build the clients cart. 
The client will send a GET request to the endpoint with the name of "cart" and receive a 
dictionary with the keys of cart_items(holds a list of cart_items) and total_price(Remember to multiply item price by
item quantity). 
This endpoint must return the following Response status code of 200
"""
answer = {
    "cart_items": [
        {
            "id": 2,
            "item": {
                "id": 10,
                "category": "Other",
                "name": "Wireless Keyboard and Mouse",
                "price": "20.03",
            },
            "quantity": 1,
        },
        {
            "id": 3,
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
                "id": 3,
                "category": "Electronics",
                "name": "Lenovo ThinkPad",
                "price": "200.30",
            },
            "quantity": 1,
        },
        {
            "id": 5,
            "item": {
                "id": 5,
                "category": "Books",
                "name": "Cracking the Coding Interview",
                "price": "30.27",
            },
            "quantity": 1,
        },
    ],
    "total_price": 300.7,
}
"""
in order to pass the test. Pay attention to order and formatting of your data.
"""


class Test_cart_items_and_total_price(APITestCase):
    fixtures = ["items.json"]

    def test_010_cart_items_and_total_price(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        self.client.post(reverse("an_item", args=[10]))
        self.client.delete(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[10]))
        self.client.post(reverse("an_item", args=[9]))
        self.client.post(reverse("an_item", args=[3]))
        self.client.post(reverse("an_item", args=[5]))
        response = self.client.get(reverse("cart"))
        # print(response.content)
        with self.subTest():
            self.assertTrue(response.status_code ==200 and len(Cart_item.objects.all()) == 4)
        self.assertEqual(json.loads(response.content), answer)
