# -*- coding: utf-8 -*-
# @Time    : 2019-09-22-0022 1:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm

from django.contrib.auth.models import Group, Permission

from rest_framework import serializers
from users.models import *


# 学历信息（All）
class EducationAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        exclude = []


# 党团列表（读、改、写、删）
class DangTuanAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = DangTuan
        exclude = []


# 用工信息（读、改、写、删）
class YongGongAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = YongGong
        exclude = []


# 履历信息（读）
class LvLiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lvli
        exclude = []


# 车辆信息（读）
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = []


# 家庭信息（读）
class HomeInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeInformation
        exclude = []


# 个人体检信息（读）
class PhysicalExaminationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhysicalExamination
        exclude = []


# 个人量体信息（读）
class MeasureInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureInformation
        exclude = []


# 账户列表
class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        # fields = '__all__'
        exclude = ['password', ]
        depth = 1


# 未分配账户列表
class UserInformationNoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ['id', 'username']
        # exclude = ['password', ]


# 个人档案信息（改）
class PersonalInformationSerializer(serializers.ModelSerializer):
    """创建、更新、删除使用"""
    class Meta:
        model = PersonalInformation
        exclude = []


# 用工信息（读）
class YongGongSerializer(serializers.ModelSerializer):

    class Meta:
        model = YongGong
        exclude = ['name']
        depth = 1


# 党团列表（读）
class DangTuanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DangTuan
        exclude = ['name']
        depth = 1


# 学历信息（读）
class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        exclude = ['name']
        depth = 1


# 车辆信息（读）
class CarRSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = ['name']
        depth = 1


# 个人体检信息（读）
class PhysicalExaminationRSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhysicalExamination
        exclude = ['name']
        depth = 1


# 个人量体信息（读）
class MeasureInformationRSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureInformation
        exclude = ['name']
        depth = 1


# 个人档案信息(读)
class PersonalInformationListSerializer(serializers.ModelSerializer):
    """列表、单独读取使用"""
    dangtuans = DangTuanSerializer(many=True, read_only=True)
    yonggongs = YongGongSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    car = CarRSerializer(many=True, read_only=True)
    tj = PhysicalExaminationRSerializer(many=True, read_only=True)
    lt = MeasureInformationRSerializer(many=True, read_only=True)

    class Meta:
        model = PersonalInformation
        # fields = "__all__"
        exclude = []
        # extra_kwargs = {'user': {'required': False}}
        depth = 1


# 用户组列表(读)
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = []
        depth = 1


# 个人权限列表
class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        exclude = []


# 档案图片
class ImgDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImgData
        exclude = []
