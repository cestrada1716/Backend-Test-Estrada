from django.urls import path

from .views import OrderView, OrderViewPage

urlpatterns = [
    path("order", OrderView.as_view(), name="order"),
    path("order_view", OrderViewPage.as_view(), name="order_view"),
]
