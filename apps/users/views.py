from django.contrib.auth.models import Group, Permission

# from django.shortcuts import render

# Create your views here.
# from rest_framework.generics import get_object_or_404

from .models import PersonalInformation, UserInformation, Role
from classification.models import *
from .serializers import *
# from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins, status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
# 重构token登录验证返回
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

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
    create:创建个人信息,user字段如果需要自己创建请填写1（int类型的）
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
    search_fields = ['name', 'named', 'idnumber']

    # drf排序设置
    ordering_fields = ['category']

    def get_queryset(self):
        """设置列表返回数据"""
        if self.request is not None:
            username = self.request.user
            if self.request.user.is_superuser:
                '''允许超级管理员查看全部信息'''
                return PersonalInformation.objects.filter(is_delete=False)
            else:
                role_fenzu = DaduiZhongduiType.objects.filter(role__users=username)

                if role_fenzu:
                    '''大队、中队、小组权限显示'''
                    return PersonalInformation.objects.filter(is_delete=False, fenzu__in=role_fenzu)
                else:
                    '''权限范围到个人，只有本账号访问权限'''
                    return PersonalInformation.objects.filter(is_delete=False, user=username)

    def create(self, request, *args, **kwargs):
        """重写创建数据方法，在创建数据时判断是否有本人身份证创建的账号，如无则创建一个账号，并关联"""
        idnumber = request.data['idnumber']
        if request.data['user'] == 1:
            if not UserInformation.objects.filter(username=idnumber):
                user = UserInformation.objects.create_user(username=idnumber, password='Tjzd68316070.')
                user.last_name = request.data['name'][0]
                user.first_name = request.data['name'][1:]
                user.save()
                request.data['user'] = user.id
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                if UserInformation.objects.filter(personalinformation=None, username=idnumber):
                    user = UserInformation.objects.get(username=idnumber)
                    request.data['user'] = user.id
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                return Response(
                    {'status': 500, 'message': '%s用户数据已存在' % idnumber},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserInformationList(viewsets.ModelViewSet):
    """list：个人信息"""
    queryset = UserInformation.objects.filter(is_superuser=False)
    serializer_class = UserInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    def get_queryset(self):
        """设置列表返回数据"""
        if self.request is not None:
            username = self.request.user
            if self.request.user.is_superuser:
                '''允许超级管理员查看全部信息'''
                return UserInformation.objects.filter(is_active=True)
            else:
                role_fenzu = DaduiZhongduiType.objects.filter(role__users=username)

                if role_fenzu:
                    '''大队、中队、小组权限显示'''
                    return UserInformation.objects.filter(is_active=True, fenzu__in=role_fenzu)
                else:
                    '''权限范围到个人，只有本账号访问权限'''
                    return UserInformation.objects.filter(is_active=True, user=username)


class UserInformationNoneList(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    list:未分配用户账号
    """
    queryset = UserInformation.objects.filter(is_superuser=False, personalinformation=None, is_active=True)
    serializer_class = UserInformationNoneSerializer
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
                         '用户组': user_data.user_permissions.all(), 'superuser': user_data.is_superuser
                         })
