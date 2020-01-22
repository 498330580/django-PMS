from django.contrib.auth.models import Group, Permission

# from django.shortcuts import render

# Create your views here.

from .models import PersonalInformation, UserInformation
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


class PersonalInformationList(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    List:
        个人信息列表页.
    """
    # queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       filters.SearchFilter,  # drf模糊查询
                       filters.OrderingFilter  # drf排序设置
                       ]

    # django_filters过滤
    # filterset_fields = ['name', 'category']
    filter_class = PersonalInformationFilter

    # drf模糊查询
    search_fields = ['name', 'named']

    # drf排序设置
    ordering_fields = ['category']

    def get_queryset(self):
        group_name = ''
        if Group.objects.filter(user=self.request.user):
            group_name = Group.objects.get(user=self.request.user).name
        username = self.request.user
        if self.request.user.is_superuser:
            '''允许超级管理员查看全部信息'''
            return PersonalInformation.objects.all()
        elif group_name in ['人事管理']:
            '''允许具有人事管理的人员查看全部未被标记删除的人员信息'''
            return PersonalInformation.objects.filter(delete=False)
        else:
            '''其他用户查看本人信息'''
            return PersonalInformation.objects.filter(user=username)

    # def put(self, request, pk, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# class PersonalInformationList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         personalinformation = PersonalInformation.objects.all()[:10]
#         serializer = PersonalInformationSerializer(personalinformation, many=True)
#         return Response(serializer.data)


class UserInformationList(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """List：个人信息"""
    queryset = UserInformation.objects.filter(is_superuser=False)
    serializer_class = UserInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class GroupList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        List:用户组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class PermissionList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
     List:权限列表
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
