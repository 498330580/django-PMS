# -*- coding: utf-8 -*-
# @Time    : 2019-09-22-0022 1:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm

from django.contrib.auth.models import Group, Permission

from rest_framework import serializers
from .models import PersonalInformation, UserInformation


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        # fields = '__all__'
        exclude = ['password', ]


class PersonalInformationSerializer(serializers.ModelSerializer):
    # user = UserInformationSerializer(many=False, read_only=False)

    # images = GoodsImageSerializer(many=True)
    class Meta:
        model = PersonalInformation
        # fields = "__all__"
        exclude = []
        # extra_kwargs = {'user': {'required': False}}

        # depth = 1


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = []


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        exclude = []
