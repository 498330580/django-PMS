# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
# from django.db.models import Q

from users.models import PersonalInformation


class PersonalInformationFilter(django_filters.rest_framework.FilterSet):
    """
    人员的过滤类
    """
    # timestart = django_filters.DateTimeFilter(field_name='entry', help_text="开始时间", lookup_expr='gte')
    # timeout = django_filters.DateTimeFilter(field_name='entry', help_text="结束时间", lookup_expr='lte')
    # category = django_filters.CharFilter(field_name='category__name', help_text='人员类别', lookup_expr='icontains')
    # name = django_filters.CharFilter(field_name='name', help_text='名字', lookup_expr='icontains')
    # dadui = django_filters.CharFilter(field_name='dadui', help_text='大队', lookup_expr='icontains')
    # fenzu_dadui = django_filters.CharFilter(field_name='fenzu__name', help_text='大队', lookup_expr='icontains')
    # fenzu_zhongdui = django_filters.CharFilter(field_name='fenzu__name', help_text='中队、小组', lookup_expr='icontains')

    # top_category = django_filters.NumberFilter(method='top_category_filter')
    #
    # def top_category_filter(self, queryset, name, value):
    #     return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
    #         category__parent_category__parent_category_id=value))

    class Meta:
        model = PersonalInformation
        # fields = ['name', 'category', 'entry']
        fields = ['dadui', 'fenzu']
