# import user models
from modules.users.models import UserCornershop


def create_user(data: dict) -> UserCornershop:
    """
    `Create a new user in the system.
    """
    user = UserCornershop(**data)
    user.username = data["email"]
    user.is_superuser = False
    user.set_password(data["password"])
    user.save()
    return user
