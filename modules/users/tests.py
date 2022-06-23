# import django rest framework modules
from django.test import TestCase
from rest_framework import status

# Django Rest Framework test modules
from rest_framework.test import APIClient, APIRequestFactory

# import models from users app
from modules.users.models import UserCornershop
from modules.users.views import UserView


class UsersTest(TestCase):
    base_url = "/cornershop_food/api/v1/"

    def setUp(self):
        user = UserCornershop(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            full_name="Test",
            slack_id="Test",
            phone_number="Test",
            user_type="employee",
            username="Test",
            email="carlos@gmail.com",
        )
        user.set_password("Test")
        user.save()

    def test_create_user_when_no_admin_user_expect_bad_request(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + "users", {})
        response = UserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            str(response.data["message"]["full_name"].pop()), "This field is required."
        )
        self.assertEqual(
            str(response.data["message"]["slack_id"].pop()), "This field is required."
        )
        self.assertEqual(
            str(response.data["message"]["phone_number"].pop()),
            "This field is required.",
        )
        self.assertEqual(
            str(response.data["message"]["email"].pop()), "This field is required."
        )

    def test_create_user_when_user_exists_expect_status_bad_request(self):
        factory = APIRequestFactory()
        request = factory.post(
            self.base_url + "users",
            {
                "full_name": "Test",
                "slack_id": "Test",
                "phone_number": "Test",
                "email": "carlos@gmail.com",
            },
        )
        response = UserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_when_expect_status_ok(self):
        factory = APIRequestFactory()
        request = factory.post(
            self.base_url + "users",
            {
                "full_name": "Test",
                "slack_id": "Test",
                "phone_number": "Test",
                "email": "xcarlos@gmail.com",
                "user_type": "employee",
                "username": "Test",
                "password": "Test",
            },
        )
        response = UserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
