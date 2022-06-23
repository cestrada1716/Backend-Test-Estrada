# import python modules
import datetime

# import django serializers
from rest_framework import serializers

# import models from another appd
from modules.menu.models import Menu, Option
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
    quantity = serializers.IntegerField()
    commentary = serializers.CharField(max_length=500, default=None, required=False)

    class Meta:
        model = Order
        fields = ("id", "menu", "quantity", "created_at", "option", "commentary")

    def validate(self, attrs):
        if datetime.datetime.now().hour >= 19:
            raise serializers.ValidationError({"menu": "Order must be before 11 am"})
        if attrs["menu"] not in Menu.objects.all():
            raise serializers.ValidationError({"menu": "Menu does not exist"})
        if attrs["quantity"] < 1:
            raise serializers.ValidationError(
                {"quantity": "Quantity must be greater than 0"}
            )
        if attrs["option"] not in Option.objects.all():
            raise serializers.ValidationError({"option": "Option does not exist"})
        if attrs["option"] not in attrs["menu"].options.all():
            raise serializers.ValidationError(
                {"option": "Option does not belong to menu"}
            )
        return attrs
