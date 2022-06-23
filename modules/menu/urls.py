# import django urls
from django.urls import path

# import views from this module
from .views import DetailMenuView, DetailOptionView, MenuView, MenuViewData, OptionView

urlpatterns = [
    path("option", OptionView.as_view(), name="option"),
    path("option/<uuid:pk>", DetailOptionView.as_view(), name="detail_option"),
    path("menu", MenuView.as_view(), name="menu"),
    path("menu/<uuid:pk>", DetailMenuView.as_view(), name="detail_menu"),
    path("menu/view/<uuid:pk>", MenuViewData.as_view(), name="menu_view"),
]
