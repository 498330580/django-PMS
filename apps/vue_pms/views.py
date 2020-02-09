# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from vue_pms.models import Menu
from vue_pms.serializers import MenuSerializer


class MenuViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        菜单列表数据
    """
    queryset = Menu.objects.filter(category_type=1).filter(is_look=True)
    serializer_class = MenuSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
