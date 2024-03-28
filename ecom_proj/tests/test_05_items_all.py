from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json


"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will set the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

The user will then send a GET request to the endpoint name "all_items".
This endpoint must return the following Response status code of 200
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
        "id": 4,
        "category": "Books",
        "name": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "price": "250.57"
    },
    {
        "id": 5,
        "category": "Books",
        "name": "Cracking the Coding Interview",
        "price": "30.27"
    },
    {
        "id": 6,
        "category": "Books",
        "name": "Python Crash Course",
        "price": "30.01"
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
    },
    {
        "id": 9,
        "category": "Other",
        "name": "Code Editor Subscription",
        "price": "50.10"
    },
    {
        "id": 10,
        "category": "Other",
        "name": "Wireless Keyboard and Mouse",
        "price": "20.03"
    },
    {
        "id": 11,
        "category": "Other",
        "name": "Notepad and Pen Set",
        "price": "15.34"
    }
]

"""
In order to pass the test. Pay attention to order and formatting of your data.
"""

class Test_all_items(APITestCase):
    fixtures=["items.json"]

    def test_005_all_items(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("all_items"))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)