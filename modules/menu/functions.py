# imports python modules
import uuid
from datetime import date
from typing import Any

# import django settings
from django.conf import settings

# import menu model from Menu module
from modules.menu.models import Menu


def build_menu_url(menu_id: uuid.UUID) -> str:
    """
    Builds a url for the menu with the given id.
    """
    return settings.MENU_URL + str(menu_id)


def get_menu_id_today() -> Any:
    """
    Returns the id of the menu for today.
    """
    menu = Menu.objects.get(menu_date=date.today())
    if menu:
        return menu.id
    return None
