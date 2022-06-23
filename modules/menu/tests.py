from django.test import TestCase
from modules.menu.models import Menu, Option
from modules.users.models import UserCornershop
from modules.menu.views import MenuView, DetailMenuView, OptionView, DetailOptionView
# Django Rest Framework
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status


class MenuTestCase(TestCase):
    base_url = '/cornershop_food/api/v1/'

    def setUp(self):
        menu = Menu(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            name="Test",
            menu_date="2022-06-22"
        )
        menu.save()
        option = Option(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            name="Test",
            price=10.0,
            description="Test"
        )
        option.save()

        user = UserCornershop(
            id="2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            full_name="Test",
            slack_id="Test",
            phone_number="Test",
            user_type="employee",
            username="Test",
            email="test@gmail.com"
        )
        user.set_password("Test")
        user.save()

    def test_get_menus_when_not_logged_expect_forbidden(self):
        client = APIClient()
        response = client.get(self.base_url + 'menu', {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_menus_when_no_admin_user_expect_forbidden(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + 'menu')
        request.session = {"user_type": "employee"}
        response = MenuView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_menus_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + 'menu')
        request.session = {"user_type": "admin"}
        response = MenuView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], "2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a")

    def test_create_menu_no_data_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + 'menu', {})
        request.session = {"user_type": "admin"}
        response = MenuView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['name'][0]), "This field is required.")
        self.assertEqual(str(response.data['menu_date'][0]), "This field is required.")

    def test_create_menu_with_data_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + 'menu',
                               self.build_fake_menu_data(name="Test", menu_date="2022-06-24",
                                                         options=["2bc0dfa4-e7f3-4c5a-a0d0"
                                                                  "-76977fc10a7a"]))
        request.session = {"user_type": "admin"}
        response = MenuView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test')

    def test_get_menu_data_when_no_admin_user_expect_forbidden(self):
        factory = APIRequestFactory()
        request = factory.put(self.base_url + 'menu/2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a', {})
        request.session = {"user_type": "employee"}
        response = DetailMenuView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_menu_data_when_empty_data_expect_bad_request(self):
        factory = APIRequestFactory()
        request = factory.put(self.base_url + 'menu/2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a', {"id": "2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a"})
        request.session = {"user_type": "admin"}
        response = DetailMenuView.as_view()(request, pk='2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['name'][0]), "This field is required.")
        self.assertEqual(str(response.data['menu_date'][0]), "This field is required.")

    def test_get_menu_data_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.put(self.base_url + 'menu/2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a',
                              self.build_fake_menu_data(name="Test", menu_date="2032-06-22",
                                                        options=["2bc0dfa4-e7f3-4c5a-a0d0"
                                                                 "-76977fc10a7a"]))
        request.session = {"user_type": "admin"}
        response = DetailMenuView.as_view()(request, pk='2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test')

    def test_get_options_when_no_admin_user_expect_forbidden(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + 'options')
        request.session = {"user_type": "employee"}
        response = OptionView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_options_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.get(self.base_url + 'options')
        request.session = {"user_type": "admin"}
        response = OptionView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], "2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a")

    def test_create_option_no_data_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + 'options', {})
        request.session = {"user_type": "admin"}
        response = OptionView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data['name'][0]), "This field is required.")

    def test_create_option_with_data_when_admin_user_expect_statusOK(self):
        factory = APIRequestFactory()
        request = factory.post(self.base_url + 'options',
                               self.build_fake_option_data(name="Test", price=10, description="Test"))
        request.session = {"user_type": "admin"}
        response = OptionView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test')

    def build_fake_menu_data(self, name, menu_date, options):
        return {
            "id": "2bc0dfa4-e7f3-4c5a-a0d0-76977fc10a7a",
            "name": name,
            "options": options,
            "menu_date": menu_date
        }

    def build_fake_option_data(self, name, price, description):
        return {
            "name": name,
            "price": price,
            "description": description
        }