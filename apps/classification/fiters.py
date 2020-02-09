# -*- coding: utf-8 -*-
# @Time    : 2020-02-08-0008 22:06
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : fiters.py
# @Software: PyCharm

import django_filters
from classification.models import DaduiZhongduiType


class DaduiZhongduiTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = DaduiZhongduiType
        # fields = ['name', 'category', 'entry']
        fields = ['category_type', 'parent_category']
