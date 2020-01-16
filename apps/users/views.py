from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.

from apps.users.models import PersonalInformation
from .serializers import PersonalInformationSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from django_filters.rest_framework import DjangoFilterBackend
# 重构token登录验证返回
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .filters import PersonalInformationFilter


class PersonalInformationPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class PersonalInformationList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List:
        个人信息列表页.
    """
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
    pagination_class = PersonalInformationPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication)  # 接口登录验证
    permission_classes = (DjangoObjectPermissions, IsAuthenticated)

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
        group_name = Group.objects.get(user=self.request.user).name
        username = self.request.user
        if self.request.user.is_superuser or group_name in ['人事管理']:
            return PersonalInformation.objects.all()
        else:
            return PersonalInformation.objects.filter(user=username)


# class PersonalInformationList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         personalinformation = PersonalInformation.objects.all()[:10]
#         serializer = PersonalInformationSerializer(personalinformation, many=True)
#         return Response(serializer.data)

class PersonalInformationAdd(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """添加个人信息"""
    pass


class Login(ObtainAuthToken):
    """修改登录返回格式"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'status': HTTP_200_OK})

