from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Menu
from menu.serializers import MenuSerializer


class MenuListView(ListView):
    model = Menu
    template_name = 'menu/index.html'
    all_menus = Menu.objects.all()
    queryset = list(filter(lambda menu: menu.dishes.exists(), all_menus))


class MenuDetailView(APIView):
    def get(self, *args, **kwargs):
        menu = get_object_or_404(Menu, pk=kwargs['pk'])
        serialized_data = MenuSerializer(menu).data
        return Response(serialized_data)
