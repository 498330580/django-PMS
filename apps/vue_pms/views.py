# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from vue_pms.models import Menu, WebsiteConfig
from vue_pms.serializers import MenuSerializer, ConfigSerializer, MenuSerializerList, MenuSerializerConfig


class MenuViewset(viewsets.ModelViewSet):
    """
    list:菜单列表数据
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    # 动态分配serializer
    def get_serializer_class(self):
        if self.action == "list":
            if 'type' in self.request.query_params:
                if self.request.query_params['type'] == 'menu':
                    return MenuSerializer
                elif self.request.query_params['type'] == 'modify':
                    return MenuSerializerList
                else:
                    return MenuSerializer
            else:
                if self.request.user.is_superuser:
                    return MenuSerializerConfig
                else:
                    return MenuSerializer
        else:
            return MenuSerializerList

    def get_queryset(self):
        if 'type' in self.request.query_params:
            if self.request.query_params['type'] == 'menu':
                return Menu.objects.filter(category_type=1).filter(is_look=True)
            elif self.request.query_params['type'] == 'modify':
                return Menu.objects.all()
            else:
                return Menu.objects.filter(category_type=1).filter(is_look=True)
        else:
            if self.request.user.is_superuser:
                return Menu.objects.filter(category_type=1)
            else:
                return Menu.objects.filter(category_type=1).filter(is_look=True)


class Config(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """
    retrieve:读取网站设置
    update:更新网站设置
    """
    queryset = WebsiteConfig.objects.all()
    serializer_class = ConfigSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    def retrieve(self, request, *args, **kwargs):
        # instance = self.get_object()
        instance = WebsiteConfig.objects.get(id=1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
