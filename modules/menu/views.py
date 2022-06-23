# import python modules
from datetime import date

# import swagger models
from drf_yasg.utils import swagger_auto_schema

# import rest framework modules
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# import permissions class
from backend_test.permissions import RoleUserPermission

# import menu and orders modules and serializers
from .models import Menu, Option
from .serializers import MenuSerializer, OptionSerializer


@swagger_auto_schema(operation_description="Get and create options")
class OptionView(APIView):
    """
    This class handles the creation of a new option and
    retrive all options in the system.
    Method: POST, GET
    URL: cornershop_food/api/v1/options/
    :param request
    :return: Response (rest_framework.response object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        options = Option.objects.all()
        return Response(OptionSerializer(options, many=True).data)

    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="Update an option")
class DetailOptionView(APIView):
    """
    This class handles the update of an option.
    Method: PUT
    URL: cornershop_food/api/v1/options/<int:pk>/
    :param request
    :param pk
    :return: Response (rest_framework.response object)
    """

    permission_classes = (RoleUserPermission,)

    def put(self, request, pk):
        try:
            serializer = OptionSerializer(Option.objects.get(pk=pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Option.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(operation_description="Get and create menus")
class MenuView(APIView):
    """
    This class handles the creation of a new menu and
    retrive all menus in the system.
    Method: POST, GET
    URL: cornershop_food/api/v1/menu/
    :param request
    :return: Response (rest_framework.response object)
    """

    permission_classes = (RoleUserPermission,)

    def get(self, request):
        menus = Menu.objects.all()
        return Response(MenuSerializer(menus, many=True).data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="Update a menu")
class DetailMenuView(APIView):
    """
    This class handles the update of a menu.
    Method: PUT
    URL: cornershop_food/api/v1/menu/<int:pk>/
    :param request
    :param pk
    :return: Response (rest_framework.response object)
    """

    permission_classes = (RoleUserPermission,)

    def put(self, request, pk):
        try:
            if "id" not in request.data:
                request.data["id"] = pk
            serializer = MenuSerializer(Menu.objects.get(pk=pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(operation_description="Update a menu")
class MenuViewData(APIView):
    """
    This class handles the render of a menu page.
    Method: GET
    URL: cornershop_food/api/v1/menu/<int:pk>/
    :param request
    :param pk
    :return: render (django.shortcuts  object)
    """

    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            menus = Menu.objects.get(pk=pk)
            if menus:
                if menus.menu_date == date.today():
                    return render(request, "menu.html", {"menus": menus})
            return Response(
                {"this menu is not aviable"}, status=status.HTTP_404_NOT_FOUND
            )
        except Menu.DoesNotExist:
            return Response(
                {"this menu is not aviable"}, status=status.HTTP_404_NOT_FOUND
            )
