from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

The client will then send a GET request to the endpoint of name "an_item" with the
number 10 being passed as the item_id.
This endpoint must return the following Response status code of 200
"""

answer = {
    "id": 10,
    "category": "Other",
    "name": "Wireless Keyboard and Mouse",
    "price": "20.03"
}

"""
In order to pass the test. Pay attention to order and formatting of your data.
"""

class Test_item_by_id(APITestCase):
    fixtures=["items.json"]

    def test_007_item_by_id(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("an_item", args=[10]))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)