# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets

from .models import Menu
from .serializers import MenuSerializer


class MenuViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = Menu.objects.filter(category_type=1)
    serializer_class = MenuSerializer
