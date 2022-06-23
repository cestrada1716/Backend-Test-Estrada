# import django urls
from django.urls import path

# import views from this app
from .views import LoginViewPage, UserView

urlpatterns = [
    path("login_view", LoginViewPage.as_view(), name="login_view"),
    path("users", UserView.as_view(), name="users"),
]
