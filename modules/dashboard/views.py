# import django and rest framework
from django.shortcuts import render
from rest_framework.views import APIView

# import Views menu and orders modules
from backend_test.permissions import RoleUserPermission
from modules.menu.views import MenuView, OptionView
from modules.orders.views import OrderView

# import swagger models
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="orders page")
class OrderDashboardPage(APIView):
    """
    This class handles the render of get orders page.
    Method: GET
    URL: cornershop_food/api/v1/orders/
    :param request
    :return: render (django.shortcuts  object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        response = OrderView.get(self, request)
        return render(request, "orders.html", {"response": response.data})


@swagger_auto_schema(operation_description="menu page")
class MenuDashboardPage(APIView):
    """
    This class handles the render of get menu page.
    Method: GET
    URL: cornershop_food/api/v1/menu/
    :param request
    :return: render (django.shortcuts  object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        response = MenuView.get(self, request)
        return render(request, "menu_dashboard.html", {"response": response.data})


@swagger_auto_schema(operation_description="options page")
class OptionsDashboardPage(APIView):
    """
    This class handles the render of get options page.
    Method: GET
    URL: cornershop_food/api/v1/options/
    :param request
    :return: render (django.shortcuts  object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        response = OptionView.get(self, request)
        return render(request, "options.html", {"response": response.data})
