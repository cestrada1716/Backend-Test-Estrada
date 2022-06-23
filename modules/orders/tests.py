# impot rest framework modules
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory

# import python modules
from freezegun import freeze_time

# import modules and views from another apps
from modules.menu.models import Menu, Option
from modules.orders.models import Order
from modules.orders.views import OrderView


class OrderTestCase(TestCase):
    base_url = "/cornershop_food/api/v1/"

    def setUp(self):
        menu = Menu(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            name="Test",
            menu_date="2022-06-22",
        )
        menu.save()

        option = Option(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            name="Test",
            price=10.0,
            description="Test",
        )
        option.save()

        order = Order(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            option=option,
            menu=menu,
            quantity=1,
            commentary=1,
        )
        order.save()

    def test_get_orders_when_not_logged_expect_forbidden(self):
        client = APIClient()
        response = client.get(self.base_url + "order", {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_orders_when_no_admin_user_expect_forbidden(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + "order")
        request.session = {"user_type": "employee"}
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_orders_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + "order")
        request.session = {"user_type": "admin"}
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], "2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a")

    @freeze_time("2042-01-14 23:21:34")
    def test_create_order_after_11_am_when_admin_user_expect_bad_request(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + "order", self.build_fake_order_data())
        request.session = {"user_type": "admin"}
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @freeze_time("2042-01-14 03:21:34")
    def test_create_order_no_data_when_admin_user_expect_statusCreated(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + "order", self.build_fake_order_data())
        request.session = {"user_type": "admin"}
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def build_fake_order_data(self):
        option = Option(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7b",
            name="Test",
            price=10.0,
            description="Test",
        )
        option.save()

        menu = Menu(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7b",
            name="Test",
            menu_date="2022-06-22",
        )
        menu.save()
        menu.options.set([option])

        return {"option": option.id, "menu": menu.id, "quantity": 1, "commentary": 1}
