from rest_framework import serializers

from menu.models import Dish, Menu


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name',)


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('name', 'description', 'dishes')
