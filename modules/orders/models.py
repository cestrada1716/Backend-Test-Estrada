# import python modules
import uuid

# import django models
from django.db import models

# import models from menu app
from modules.menu.models import Menu, Option


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    commentary = models.CharField(max_length=500, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu.name
