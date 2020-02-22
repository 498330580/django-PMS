# from django.views.generic.base import View

from users.models import *
from django.apps import apps
# from classification.models import DaduiZhongduiType
from users.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import Group, Permission
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
from rest_framework.status import HTTP_200_OK

from .filters import *


# 个人信息自定义分页器
class PersonalInformationPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 1000


# 个人信息
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
    # serializer_class = PersonalInformationSerializer
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

    # lookup_field = 'idnumber'  # 单个数据读取字段

    # django_filters过滤
    # filterset_fields = ['name', 'category']
    filter_class = PersonalInformationFilter

    # drf模糊查询
    search_fields = ['name', 'named', 'idnumber']

    # drf排序设置
    ordering_fields = ['dadui', ]

    # 动态分配serializer
    def get_serializer_class(self):
        if self.action == "list":
            return PersonalInformationListSerializer
        else:
            return PersonalInformationSerializer

    def get_queryset(self):
        """设置列表返回数据"""
        if self.request is not None and self.request.user.has_perm('users.view_personalinformation'):
            PersonalInformation.objects.filter(yonggongs__end__isnull=True)
            username = self.request.user
            if self.request.user.is_superuser or self.request.user.is_staff:
                '''允许超级管理员/可登录后台用户查看全部信息查看全部信息'''
                return PersonalInformation.objects.all()
            else:
                # role_fenzu = DaduiZhongduiType.objects.filter(role__users=username)
                # role_fenzu = DaduiZhongduiType.objects.filter(role__user__username=username.username)
                role_fenzu = self.request.user.fenzu.all()

                if role_fenzu:
                    '''大队、中队、小组权限显示'''
                    PersonalInformation.objects.filter()
                    return PersonalInformation.objects.filter(is_delete=False, fenzu__in=role_fenzu)
                else:
                    '''权限范围到个人，只有本账号访问权限'''
                    return PersonalInformation.objects.filter(is_delete=False, user=username)
        else:
            return PersonalInformation.objects.filter(user='1')

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
                    {'status': 406, 'message': '%s用户数据已存在' % idnumber},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """重写前端删除方法"""
        instance = self.get_object()
        user = UserInformation.objects.get(personalinformation=instance)
        if request.user.is_superuser or request.user.is_staff:
            if request.query_params['del'] == 'false':
                """删除"""
                # 标记个人档案删除
                instance.is_delete = True
                instance.save()
                # 标记用户信息删除（不可登录）
                user.is_active = False
                user.save()
                # 标记用工信息删除
                YongGong.objects.filter(name=instance).update(is_delete=True)
                # 标记党团信息删除
                DangTuan.objects.filter(name=instance).update(is_delete=True)
                # 标记履历信息删除
                Lvli.objects.filter(name=instance).update(is_delete=True)
                # 标记学历信息删除
                Education.objects.filter(name=instance).update(is_delete=True)
                # 标记车辆信息删除
                Car.objects.filter(name=instance).update(is_delete=True)
                # 标记家庭信息删除
                HomeInformation.objects.filter(name=instance).update(is_delete=True)
                # 标记体检信息删除
                PhysicalExamination.objects.filter(name=instance).update(is_delete=True)
                # 标记量体信息删除
                MeasureInformation.objects.filter(name=instance).update(is_delete=True)
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif request.query_params['del'] == 'true':
                """真删除"""
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif request.query_params['del'] == 'no':
                """取消删除"""
                instance.is_delete = False
                instance.save()
                user.is_active = True
                user.save()
                YongGong.objects.filter(name=instance).update(is_delete=False)
                DangTuan.objects.filter(name=instance).update(is_delete=False)
                Lvli.objects.filter(name=instance).update(is_delete=False)
                Education.objects.filter(name=instance).update(is_delete=False)
                Car.objects.filter(name=instance).update(is_delete=False)
                HomeInformation.objects.filter(name=instance).update(is_delete=False)
                PhysicalExamination.objects.filter(name=instance).update(is_delete=False)
                MeasureInformation.objects.filter(name=instance).update(is_delete=False)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                """不存在"""
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # if request.user.is_superuser and False:
        #     if UserInformation.objects.get(personalinformation=instance).delete():
        #         return Response(status=status.HTTP_204_NO_CONTENT)
        #     else:
        #         return Response(status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     # self.perform_destroy(instance)
        #     return Response(status=status.HTTP_204_NO_CONTENT)


# 权限验证
def permission_verify(user, keys, remove=None):
    permission_dic = {}
    modellist = [i._meta.verbose_name for i in apps.get_app_config(keys).get_models()]
    if remove:
        modellist.remove(remove)
    modelcount = len(modellist)
    addcount = 0
    viewcount = 0
    changecount = 0
    deletecount = 0
    for i in Permission.objects.all():
        # print(i.name.split()[-1])
        if i.name.split()[-1] in modellist and user.has_perm('{}.{}'.format(keys, i.codename)):
            # print(i.name.split()[-1], user.has_perm('{}.{}'.format(keys, i.codename)))
            if i.name.split()[-2] == 'add':
                addcount += 1
            elif i.name.split()[-2] == 'view':
                viewcount += 1
            elif i.name.split()[-2] == 'change':
                changecount += 1
            elif i.name.split()[-2] == 'delete':
                deletecount += 1
    # print(modelcount, addcount, viewcount, changecount, deletecount)
    permission_dic['{}add'.format(keys)] = True if addcount == modelcount else False
    permission_dic['{}view'.format(keys)] = True if viewcount == modelcount else False
    permission_dic['{}change'.format(keys)] = True if changecount == modelcount else False
    permission_dic['{}delete'.format(keys)] = True if deletecount == modelcount else False
    return permission_dic


# 个人账户信息
class UserInformationList(viewsets.ModelViewSet):
    """
    list：个人账号信息
    """
    # queryset = UserInformation.objects.filter(is_superuser=False)
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
                return UserInformation.objects.all()
            else:
                # role_fenzu = DaduiZhongduiType.objects.filter(role__users=username)
                # role_fenzu = DaduiZhongduiType.objects.filter(role__user__username=username.username)
                # role_fenzu = self.request.user.groups.all()
                role_fenzu = self.request.user.fenzu.all()

                if role_fenzu:
                    '''大队、中队、小组权限显示'''
                    return UserInformation.objects.filter(is_active=True, personalinformation__fenzu__in=role_fenzu)
                else:
                    '''权限范围到个人，只有本账号访问权限'''
                    return UserInformation.objects.filter(is_active=True, username=username.username)

    def retrieve(self, request, *args, **kwargs):
        """重写读取方法"""
        instance = self.get_object()
        if 'permission' in self.request.query_params:
            permission = self.request.query_params['permission']
            if permission == 'users':
                return Response(permission_verify(instance, 'users'))

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# 个人账户信息（未关联账户）
class UserInformationNoneList(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    list:未分配用户账号
    """
    queryset = UserInformation.objects.filter(is_superuser=False, personalinformation=None, is_active=True)
    serializer_class = UserInformationNoneSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


# 用户组
class GroupList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        list:用户组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


# 所有权限
class PermissionList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
     list:权限列表
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


# 登录接口
class Login(ObtainAuthToken):
    """修改登录返回格式"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # user_data = UserInformation.objects.get(username=user.username)
        return Response({'token': token.key, 'status': HTTP_200_OK, 'ID': user.id, 'staff': user.is_staff,
                         '用户名': user.username, '姓': user.last_name, '名': user.first_name,
                         # '用户组': user.user_permissions.all(),
                         'superuser': user.is_superuser
                         })


# 民族列表
class Nation(APIView):
    """
    list:民族列表
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     import json
    #     from django.core import serializers
    #     from django.http import HttpResponse, JsonResponse
    #     nationdata = [{'name': nation[0], 'value': nation[1]} for nation in NATION]
    #     print(nationdata)
    #     # json_data = serializers.serialize('json', nationdata)
    #     # json_data = json.loads(json_data)
    #     return HttpResponse(json.dumps(nationdata), content_type='application/json')
    #     # return Response(nationdata)

    def get(self, request):
        """
        list:民族列表
        """
        nationdata = [{'name': nation[0], 'value': nation[1]} for nation in NATION]
        return Response(nationdata)


# 党团关系
class DangTuanList(viewsets.ModelViewSet):
    """
    list:党团关系
    """
    queryset = DangTuan.objects.filter(is_delete=False)
    serializer_class = DangTuanAllSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = DangTuanFilter

    # # 动态分配serializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return DangTuanSerializer
    #     else:
    #         return DangTuanAllSerializer


# 用工信息
class YongGongList(viewsets.ModelViewSet):
    """
    list:用工信息
    """
    queryset = YongGong.objects.filter(is_delete=False)
    serializer_class = YongGongAllSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = YongGongFilter


# 履历信息
class LvLiList(viewsets.ModelViewSet):
    """
    list:履历信息
    """
    queryset = Lvli.objects.filter(is_delete=False)
    serializer_class = LvLiSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = LvLiFilter


# 学历信息
class EducationList(viewsets.ModelViewSet):
    """
    list:学历信息
    """
    queryset = Education.objects.filter(is_delete=False)
    serializer_class = EducationAllSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = EducationFilter


# 车辆信息
class CarList(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    list:车辆信息
    """
    queryset = Car.objects.filter(is_delete=False)
    serializer_class = CarSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = CarFilter


# 家庭成员信息
class HomeInformationList(viewsets.ModelViewSet):
    """
    list:家庭成员信息
    """
    queryset = HomeInformation.objects.filter(is_delete=False)
    serializer_class = HomeInformationSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = HomeInformationFilter


# 个人体检信息
class PhysicalExaminationList(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    list:个人体检信息
    """
    queryset = PhysicalExamination.objects.filter(is_delete=False)
    serializer_class = PhysicalExaminationSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = PhysicalExaminationFilter


# 个人量体信息
class MeasureInformationList(viewsets.ModelViewSet):
    """
    list:个人量体信息
    """
    queryset = MeasureInformation.objects.filter(is_delete=False)
    serializer_class = MeasureInformationSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = MeasureInformationFilter


# 验证值是否属于集合当中
def jiheyanzheng(data, jihe):
    datalist = []
    for i in jihe:
        datalist.append(i[0])
    if data in datalist:
        return True
    else:
        return False


# 档案图片
class ImgDataList(viewsets.ModelViewSet):
    """
    list:档案图片
    """
    queryset = ImgData.objects.filter(is_delete=False)
    serializer_class = ImgDataSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)  # 接口登录验证
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    filter_backends = [DjangoFilterBackend,  # django_filters过滤
                       ]

    filter_class = ImgDataFilter

    def create(self, request, *args, **kwargs):
        user = self.request.user

        request.data['user'] = user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
