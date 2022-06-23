# imports django
from django.urls import path

# imports views from this module
from .views import MenuDashboardPage, OptionsDashboardPage, OrderDashboardPage

urlpatterns = [
    path("orders_dashboard", OrderDashboardPage.as_view(), name="order_dashboard"),
    path("menu_dashboard", MenuDashboardPage.as_view(), name="menu_dashboard"),
    path("options", OptionsDashboardPage.as_view(), name="options_dashboard"),
]
