# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q

from apps.users.models import PersonalInformation


class PersonalInformationFilter(django_filters.rest_framework.FilterSet):
    """
    人员的过滤类
    """
    timestart = django_filters.DateTimeFilter(field_name='entry', help_text="开始时间", lookup_expr='gte')
    timeout = django_filters.DateTimeFilter(field_name='entry', help_text="结束时间", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', help_text='人员类别', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', help_text='名字', lookup_expr='icontains')

    # top_category = django_filters.NumberFilter(method='top_category_filter')
    #
    # def top_category_filter(self, queryset, name, value):
    #     return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
    #         category__parent_category__parent_category_id=value))

    class Meta:
        model = PersonalInformation
        # fields = ['name', 'category', 'entry']
        fields = ['timestart', 'timeout', 'category', 'name']
