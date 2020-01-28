from django.contrib.auth.models import Group, Permission

# from django.shortcuts import render

# Create your views here.
# from rest_framework.generics import get_object_or_404

from .models import PersonalInformation, UserInformation, Role
from classification.models import *
from .serializers import PersonalInformationSerializer, UserInformationSerializer, GroupSerializer, PermissionSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
# 重构token登录验证返回
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK

from .filters import PersonalInformationFilter


class PersonalInformationPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class PersonalInformationList(viewsets.ModelViewSet):
    """
    list:个人信息列表页.
    retrieve:个人信息详情.
    destroy:删除个人信息.
    create:创建个人信息
    update:更新个人信息提供所有信息
    partial_update:增量更新个人信息
    """
    # queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (
        IsAuthenticated,
        DjangoModelPermissions
    )

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       filters.SearchFilter,  # drf模糊查询
                       filters.OrderingFilter  # drf排序设置
                       ]

    lookup_field = 'idnumber'  # 单个数据读取字段

    # django_filters过滤
    # filterset_fields = ['name', 'category']
    filter_class = PersonalInformationFilter

    # drf模糊查询
    search_fields = ['name', 'named']

    # drf排序设置
    ordering_fields = ['category']

    def get_queryset(self):
        """设置列表返回数据"""
        if self.request is not None:
            username = self.request.user
            ranges = [i[0] for i in Role.objects.filter(users__username=username).values_list('ranges')]
            if self.request.user.is_superuser:
                '''允许超级管理员查看全部信息'''
                return PersonalInformation.objects.all()
            else:
                if '所有' in ranges:
                    '''允许具有所有数据访问权限的人访问未被标记删除的所有数据'''
                    return PersonalInformation.objects.filter(is_delete=False)
                else:
                    '''除了超级用户，其他人都要创建档案信息，包括管理员，不然无法识别管理范围'''
                    minjing = CategoryType.objects.get(name='民警')  # 不显示管理民警内容
                    p = PersonalInformation.objects.get(user__username=username)
                    dadui = p.dadui
                    zhongdui = p.zhongdui
                    if '大队' in ranges:
                        return PersonalInformation.objects.filter(is_delete=False, dadui=dadui).exclude(
                            category=minjing)
                    elif '中队' in ranges:
                        return PersonalInformation.objects.filter(is_delete=False, dadui=zhongdui).exclude(
                            category=minjing)
                    elif '个人' in ranges:
                        '''其他用户查看本人信息'''
                        return PersonalInformation.objects.filter(user=username).exclude(category=minjing)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # Perform the lookup filtering.
    #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    #
    #     assert lookup_url_kwarg in self.kwargs, (
    #         'Expected view %s to be called with a URL keyword argument '
    #         'named "%s". Fix your URL conf, or set the `.lookup_field` '
    #         'attribute on the view correctly.' %
    #         (self.__class__.__name__, lookup_url_kwarg)
    #     )
    #
    #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    #     print(filter_kwargs)
    #     obj = get_object_or_404(queryset, **filter_kwargs)
    #     print(obj)
    #
    #     # May raise a permission denied
    #     self.check_object_permissions(self.request, obj)
    #
    #     return obj

    # def put(self, request, pk, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class UserInformationList(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """list：个人信息"""
    queryset = UserInformation.objects.filter(is_superuser=False)
    serializer_class = UserInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class GroupList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list:用户组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class PermissionList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
     list:权限列表
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class Login(ObtainAuthToken):
    """修改登录返回格式"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserInformation.objects.get(username=user)
        return Response({'token': token.key, 'status': HTTP_200_OK, 'ID': user_data.id,
                         '用户名': user_data.username, '姓': user_data.last_name, '名': user_data.first_name,
                         '用户组': user_data.user_permissions.all()
                         })
