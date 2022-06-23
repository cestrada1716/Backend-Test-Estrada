from datetime import date

# import rest_framework modules
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# import models from another apps
from backend_test.permissions import CreateOrderPermission, RoleUserPermission
from modules.menu.models import Menu, Option

# import models and serializaers from this app
from .models import Order
from .serializers import OrderSerializer

# import swagger models
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="orders view")
class OrderView(APIView):
    """
    This class handles the creation of a new order and
    retrive all orders in the system.
    Method: POST, GET
    URL: cornershop_food/api/v1/orders/
    :param request
    :return: Response (rest_framework.response object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        orders = Order.objects.all()
        return Response(OrderSerializer(orders, many=True).data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="orders view page")
class OrderViewPage(APIView):
    """
    This class handles the render of get orders page.
    Method: GET
    URL: cornershop_food/api/v1/order_view/
    :param request
    :return: render (django.shortcuts  object)
    """

    permission_classes = (CreateOrderPermission,)

    def get(self, request):
        try:
            menus = Menu.objects.get(menu_date=date.today())
            return render(request, "create-order.html", {"menus": menus})
        except Menu.DoesNotExist:
            return Response(
                {"this menu is not aviable"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        response = OrderView.post(self, request)
        return render(request, "create-order.html", {"response": response.data})
