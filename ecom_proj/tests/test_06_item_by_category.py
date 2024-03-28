from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

The client will then send a GET request to the endpoint with the name "items_by_category" 
and pass "electronics" as the Category argument. This endpoint must return the following Response status code of 200
"""

answer = [
    {
        "id": 1,
        "category": "Electronics",
        "name": "MacBook Pro",
        "price": "999.99"
    },
    {
        "id": 2,
        "category": "Electronics",
        "name": "Dell XPS 13",
        "price": "300.02"
    },
    {
        "id": 3,
        "category": "Electronics",
        "name": "Lenovo ThinkPad",
        "price": "200.30"
    },
    {
        "id": 7,
        "category": "Electronics",
        "name": "External Monitor",
        "price": "200.03"
    },
    {
        "id": 8,
        "category": "Electronics",
        "name": "Noise-Canceling Headphones",
        "price": "100.07"
    }
]

"""
In order to pass the test. Pay attention to order and formatting of your data.
"""

class Test_item_by_category(APITestCase):
    fixtures=["items.json"]

    def test_006_item_by_category(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("items_by_category", args=['electronics']))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)