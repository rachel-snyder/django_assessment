from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json
from cart_app.models import Cart_item



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

The client will then send a DELETE request to the endpoint with the name of "an_item"
and pass in the number 10 as the item_id. This will delete any Cart_Item that has a relationship
with the Item with ID of 10.
This endpoint must return the following Response status code of 204
in order to pass the test. Pay attention to order and formatting of your data.
"""

class Test_item_removed_from_cart(APITestCase):
    fixtures=["items.json"]

    def test_009_item_removed_from_cart(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        self.client.post(reverse("an_item", args=[10]))
        response = self.client.delete(reverse("an_item", args=[10]))
        with self.subTest():
            self.assertEqual(len(Cart_item.objects.all()), 0)
        self.assertEqual(response.status_code, 204)