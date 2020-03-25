# -*- coding: utf-8 -*-
# @Time    : 2019-09-22-0022 1:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from vue_pms.models import Menu, WebsiteConfig


class MenuSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer3(serializers.ModelSerializer):

    def to_representation(self, instance):
        """将从 Model 取出的数据 parse 给 Api"""
        ret = super().to_representation(instance)
        if ret['is_look']:
            return ret

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer2(serializers.ModelSerializer):
    sub_cat = MenuSerializer3(many=True)

    def to_representation(self, instance):
        """将从 Model 取出的数据 parse 给 Api"""
        ret = super().to_representation(instance)
        if ret['is_look']:
            return ret

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    sub_cat = MenuSerializer2(many=True)

    def to_representation(self, instance):
        """将从 Model 取出的数据 parse 给 Api"""
        ret = super().to_representation(instance)
        data_list = []
        for i in ret['sub_cat']:
            if i:
                data_list.append(i)
        ret['sub_cat'] = data_list
        return ret

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializerConfig3(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializerConfig2(serializers.ModelSerializer):
    sub_cat = MenuSerializerConfig3(many=True)

    class Meta:
        model = Menu
        fields = "__all__"


class MenuSerializerConfig(serializers.ModelSerializer):
    sub_cat = MenuSerializerConfig2(many=True)

    class Meta:
        model = Menu
        fields = "__all__"


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteConfig
        fields = "__all__"
