from django.test import TestCase, Client
from django.urls import reverse



"""
This test will send a post request to signup to first create a new user and then to 
the 'login' endpoint with a request body of {"email":"fr@fr.com", "password":"fr"} 
to simulate a user sending a post request to login. 

This endpoint must return the following Response

{"token":<token_generated>,"client":"fr@fr.com"} with a status code of 200 
in order to pass this test
"""


class Test_user_login_up(TestCase):
    def test_002_user_login_up(self):
        client = Client()
        client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response = client.post(
            reverse("login"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        # print(response.content)
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertTrue(
            b'"client":"fr@fr.com"' in response.content and b"token" in response.content
        )
