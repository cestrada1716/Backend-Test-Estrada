# import django modules
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# import functions from enu app
from modules.menu.functions import get_menu_id_today

# import models, functions, serializars from this app
from .functions import create_user
from .models import UserCornershop
from .serializers import CreateUserSerializer, LoginSerializer


# import swagger models
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="create user")
class UserView(APIView):
    """
  This class handles the creation of a new user and
  Method: POST
  URL: cornershop_food/api/v1/users/
  :param request
  :return: Response (rest_framework.response object)
  """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                new_user = create_user(serializer.validated_data)
                if new_user:
                    return Response(
                        {"message": "User created successfully"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"message": "User already exists"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


@swagger_auto_schema(operation_description="login page")
class LoginViewPage(APIView):
    """
    This class handles the render of a login page.
    Method: GET, POST
    URL: cornershop_food/api/v1/users/
    :param request
    :return: render (django.shortcuts  object)
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = UserCornershop.objects.get(
                    email=serializer.validated_data["email"]
                )
                is_auth = authenticate(
                    username=user.username,
                    password=serializer.validated_data["password"],
                )
                if is_auth:
                    request.session["user_type"] = user.user_type
                    request.session["menu_id"] = str(get_menu_id_today())
                    return render(
                        request, "login.html", {"message": "Login successful"}
                    )
                return render(
                    request,
                    "login.html",
                    {"message": "Login failed invalid credentials"},
                )
            except Exception as e:
                return render(
                    request,
                    "login.html",
                    {"message": "Login failed invalid credentials"},
                )
        return render(request, "login.html", {"message": serializer.errors})
