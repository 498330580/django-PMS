# -*- coding: utf-8 -*-
# @Time    : 2019-09-22-0022 1:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from .models import Menu


class MenuSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer2(serializers.ModelSerializer):
    sub_cat = MenuSerializer3(many=True)

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    sub_cat = MenuSerializer2(many=True)

    class Meta:
        model = Menu
        fields = "__all__"
