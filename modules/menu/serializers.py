# imports python modules
from datetime import date

# import rest framework modules
from rest_framework import serializers

# import menu model from Menu module
from .models import Menu, Option


class OptionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.FloatField()
    description = serializers.CharField(required=True)

    class Meta:
        model = Option
        fields = ("id", "name", "price", "description")

    def validate(self, attrs):
        if attrs["price"] < 0:
            raise serializers.ValidationError({"price": "Price must be greater than 0"})
        return attrs


class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    options = serializers.PrimaryKeyRelatedField(
        queryset=Option.objects.all(), many=True
    )
    menu_date = serializers.DateField()

    class Meta:
        model = Menu
        fields = ("id", "name", "options", "menu_date")

    def validate(self, attrs):
        if attrs["menu_date"] < date.today():
            raise serializers.ValidationError(
                {"menu_date": "Menu date must be greater than today"}
            )

        if len(attrs["options"]) < 1:
            raise serializers.ValidationError({"options": "Menu must have one option"})

        if 'id' in self.initial_data:
            if Menu.objects.filter(menu_date=attrs["menu_date"]).exclude(pk=self.initial_data["id"]).exists():
                raise serializers.ValidationError(
                    {"menu_date": "Menu for date %s already exists" % attrs["menu_date"]})
            return attrs
        if Menu.objects.filter(menu_date=attrs["menu_date"]).exists():
            raise serializers.ValidationError(
                {"menu_date": "Menu for date %s already exists" % attrs["menu_date"]})

        return attrs
