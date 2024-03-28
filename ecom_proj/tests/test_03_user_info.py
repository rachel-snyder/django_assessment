from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



"""
This test will send a post request to signup to first create a new user and 
acquire the token provided in the response. Then it will send the token under the 
AUTHORIZATION HEADER of the next request where the APIView will utilize TokenAuthentication
to authenticate the user.

This endpoint must return the following Response

{"email":"fr@fr.com"} with a status code of 200 
in order to pass this test
"""


class Test_user_info(APITestCase):
    def test_003_user_info(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("info"))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertTrue(b'{"email":"fr@fr.com"}' in response.content)
