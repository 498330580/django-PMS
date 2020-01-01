# -*- coding: utf-8 -*-
# @Time    : 2019-09-22-0022 1:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from apps.users.models import PersonalInformation, UserInformation


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ('username',)


class PersonalInformationSerializer(serializers.ModelSerializer):
    user = UserInformationSerializer()

    # images = GoodsImageSerializer(many=True)
    class Meta:
        model = PersonalInformation
        fields = "__all__"
