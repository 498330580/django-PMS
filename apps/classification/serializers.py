# -*- coding: utf-8 -*-
# @Time    : 2020-01-21-0021 20:34
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : serializers.py
# @Software: PyCharm


from rest_framework import serializers
from classification.models import *


# class CategoryTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryType
#         fields = '__all__'
#
#
# class DemobilizedTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DemobilizedType
#         fields = '__all__'
#
#
# class DrivingLicenseTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DrivingLicenseType
#         fields = '__all__'
#
#
# class DaDuiTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DaDuiType
#         fields = '__all__'
#
#
# class ZhongDuiTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ZhongDuiType
#         fields = '__all__'
#
#
# class OrganizationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ZhongDuiType
#         fields = '__all__'
#
#
# class BorrowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ZhongDuiType
#         fields = '__all__'
#
#
# class EconomicsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Economics
#         fields = '__all__'
#
#
# class SourcesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sources
#         fields = '__all__'
#
#
# class EducationTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EducationType
#         fields = '__all__'
#
#
# class AcademicDegreeTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AcademicDegreeType
#         fields = '__all__'
#
#
# class CarTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarType
#         fields = '__all__'
#
#
# class PostTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostType
#         fields = '__all__'
#
#
# class PostNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostName
#         fields = '__all__'
#
#
# class XueLiInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = XueLiInformation
#         fields = '__all__'
#
#
# class RenYuanXianZhuangSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RenYuanXianZhuang
#         fields = '__all__'
#
#
# class ShenFenGuiLeiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShenFenGuiLei
#         fields = '__all__'
#
#
# class ChengWeiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChengWei
#         fields = '__all__'
#
#
# class TiJianJieGuoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TiJianJieGuo
#         fields = '__all__'


# class YearSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Year
#         fields = '__all__'


# class DiZhiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DiZhi
#         fields = '__all__'


class TypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    introduce = serializers.CharField()
    # index = serializers.IntegerField()


class YearSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField()


# 政治面貌（读）
class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politics
        exclude = []


# 大队、中队、小组（读）
class DaduiZhongduiTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaduiZhongduiType
        exclude = []
