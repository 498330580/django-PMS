from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import Group
from dateutil.relativedelta import relativedelta
from classification.models import DiZhi

import datetime

from .tools import GetInformation

admin.AdminSite.empty_value_display = "无"  # 自定义空白显示的内容为None


# # 用户自定义模块
# class GetInformation(object):
#     """根据身份证判断生日、男女、年龄、生肖"""
#
#     def __init__(self, id):
#         self.id = id
#         self.birth_year = int(self.id[6:10])
#         self.birth_month = int(self.id[10:12])
#         self.birth_day = int(self.id[12:14])
#
#     def get_birthday(self):
#         """通过身份证号获取出生日期"""
#         birthday = "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)
#         return birthday
#
#     def get_sex(self):
#         """男生：1 女生：2"""
#         num = int(self.id[16:17])
#         if num % 2 == 0:
#             return '女'
#         else:
#             return '男'
#
#     def get_age(self):
#         """通过身份证号获取年龄"""
#         now = (datetime.datetime.now() + datetime.timedelta(days=1))
#         year = now.year
#         month = now.month
#         day = now.day
#
#         if year == self.birth_year:
#             return 0
#         else:
#             if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
#                 return year - self.birth_year - 1
#             else:
#                 return year - self.birth_year
#
#     def get_zodiac(self):
#         """通过身份证判断生肖"""
#         return '猴鸡狗猪鼠牛虎兔龙蛇马羊'[self.birth_year % 12]
#
#     def get_constellation(self):
#         n = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
#              '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
#         d = (
#             (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
#             (12, 23))
#         return n[len(list(filter(lambda y: y <= (self.birth_month, self.birth_day), d))) % 12]
#
#     def get_6(self):
#         """通过身份证获取前三位籍贯编码"""
#         return self.id[:6]


# admin后台模块
class UserInformationAdmin(UserAdmin):
    """自定义用户后台模块"""
    list_display = ('username', 'upper_case_name', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active')

    # """自定义空白显示的内容为None"""
    # empty_value_display = '-None-'

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.last_name, obj.first_name)).upper()

    upper_case_name.short_description = '姓名'

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (gettext_lazy('详细信息'), {'fields': ('last_name', 'first_name', 'email', 'qq', 'wx')}),
        (gettext_lazy('权限'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (gettext_lazy('账户记录'), {'fields': ('last_login', 'date_joined')}),
    )

    # 判断用户组，后台显示内容
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user)


# 一对多关联表编辑,让父表管理配置页面能同时编辑子表,以下的Education为子表(有外键所在的表)
class EducationInline(admin.TabularInline):
    """学历信息"""
    # Education 必须是models.py中的模型名称,大小写必须要匹配.这个模型为子表,以便可以被父表编辑
    model = Education
    # 默认显示条目的数量
    extra = 1
    exclude = ['is_delete']


class CarInline(admin.TabularInline):
    """车辆信息"""
    model = Car
    extra = 1
    exclude = ['is_delete']


class HomeInformationInline(admin.TabularInline):
    """家庭人员信息"""
    model = HomeInformation
    extra = 1
    exclude = ['is_delete']

    # 不可修改字段
    def get_readonly_fields(self, request, obj=None):
        fields = []
        current_user_set = request.user
        if request.user.is_superuser:
            return fields
        elif current_user_set.groups.all():
            current_group_set = Group.objects.get(user=current_user_set)
            if '人事管理' in str(current_group_set):
                fields = ['birthday']
                return fields
            elif '普通用户' in str(current_group_set):
                fields = ['birthday']
                return fields

    # 自动保存生日
    def save_model(self, request, obj, form, change):
        if not obj.birthday:
            shenfenzheng = form.cleaned_data['idnumber']
            getInformation = GetInformation(shenfenzheng)
            shengri = getInformation.get_birthday()
            shengri = datetime.date(*map(int, shengri.split('-')))
            obj.birthday = shengri
        obj.save()


class PhysicalExaminationInline(admin.TabularInline):
    """个人体检信息"""
    model = PhysicalExamination
    extra = 1
    exclude = ['is_delete']


class MeasureInformationInline(admin.TabularInline):
    """个人量体信息"""
    model = MeasureInformation
    extra = 1
    exclude = ['is_delete']


class PersonalinformationAdmin(admin.ModelAdmin):
    """自定义个人档案后台模块"""
    list_display = (
        'name', 'idnumber', 'sex', 'birthday', 'upper_case_age', 'permanenttype', 'dadui', 'zhongdui', 'bianzhi',
        'create_time', 'update_time', 'is_delete')  # 列表显示字段
    list_filter = ('dadui', 'zhongdui', 'politics')  # 右侧过滤栏
    list_per_page = 25  # 列表显示数据条数
    date_hierarchy = 'entry'  # 顶部显示时间索引
    list_editable = ('is_delete',)  # 列表页可编辑字段
    search_fields = ['name', 'idnumber']  # 设置搜索字段

    def get_list_filter(self, request):
        """根据权限判断显示右侧过滤栏"""
        current_user_set = request.user
        if current_user_set.groups.all():
            current_group_set = Group.objects.get(user=current_user_set)
            if '普通用户' in str(current_group_set):
                return ()
            elif '人事管理' in str(current_group_set):
                return self.list_filter
        if request.user.is_superuser:
            return self.list_filter

    def get_list_display(self, request):
        """根据权限判断列表页显示内容"""
        current_user_set = request.user
        if current_user_set.groups.all():
            current_group_set = Group.objects.get(user=current_user_set)
            if '普通用户' in str(current_group_set):
                return self.list_display[:-1]
            elif '人事管理' in str(current_group_set):
                return self.list_display
        if request.user.is_superuser:
            return self.list_display

    # 列表页显示年龄
    def upper_case_age(self, obj):
        if obj.idnumber:
            age = GetInformation(obj.idnumber).get_age()
        else:
            age = '无'
        return ("%s" % age).upper()

    upper_case_age.short_description = '年龄'

    # 自定义批量列表修改
    def make_delete(self, request, queryset):
        """
        自定义批量列表修改
        """
        if request.user.is_superuser:
            message_bit = queryset.update(is_delete=True)
            self.message_user(request, "%s 条信息被标记删除。" % message_bit)
        else:
            message_bit = '你没有权限。'
            self.message_user(request, "%s" % message_bit)

    make_delete.short_description = "标记删除"

    def make_not_delete(self, request, queryset):
        """
        自定义批量列表修改
        """
        if request.user.is_superuser:
            message_bit = queryset.update(is_delete=False)
            self.message_user(request, "%s 条信息被取消标记删除。" % message_bit)
        else:
            message_bit = '你没有权限。'
            self.message_user(request, "%s" % message_bit)

    make_not_delete.short_description = "取消标记删除"
    actions = ['make_delete', 'make_not_delete']

    # # Inline把EducationInline关联进来,让父表管理配置页面能同时编辑子表.
    inlines = [EducationInline, CarInline, HomeInformationInline, PhysicalExaminationInline, MeasureInformationInline]

    fieldsets = (
        (gettext_lazy('个人信息'), {'fields': (
            'user', 'name', 'named', 'nation', 'mobile', 'permanenttype', 'idnumber', 'sex', 'birthday', 'jiguan',
            'zodiac', 'constellation', 'permanent', 'home', 'hobby', 'politics', 'politicstime', 'drivinglicense',
            'marriage')}),
        (gettext_lazy('职务信息'), {'fields': (('entry', 'entryzhuanzheng'),
                                           ('zhuanfujing', 'fujingzhuanzheng'),
                                           'quit',
                                           ('category', 'gangweitype', 'gangweiname'),
                                           ('dadui', 'zhongdui'),
                                           ('jiediao', 'bianzhi'),
                                           'veteran')}),
        (gettext_lazy('家庭经济'), {'fields': (('economics', 'sources'),)}),
    )

    # 判断用户组，后台列表显示内容
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_user_set = request.user
        if current_user_set.groups.all():
            current_group_set = Group.objects.get(user=current_user_set)
            if '普通用户' in str(current_group_set):
                return qs.filter(user=request.user).filter(is_delete=False)
            elif '人事管理' in str(current_group_set):
                return qs.filter(is_delete=False)
        if request.user.is_superuser:
            return qs

    # 保存当前用户为默认用户
    def save_model(self, request, obj, form, change):
        if not obj.id:
            if request.user:
                obj.user = UserInformation.objects.filter(username=request.user)[0]
            shenfenzheng = form.cleaned_data['idnumber']
            getInformation = GetInformation(shenfenzheng)
            shengri = getInformation.get_birthday()
            shengri = datetime.date(*map(int, shengri.split('-')))
            xingbie = getInformation.get_sex()
            shengxiao = getInformation.get_zodiac()
            xingzuo = getInformation.get_constellation()
            jiguan = getInformation.get_6()
            dizhi = DiZhi.objects.filter(dizhi_id=jiguan)
            if dizhi:
                obj.jiguan = dizhi[0]
            if form.cleaned_data['entry']:
                ruzhishijian = form.cleaned_data['entry']
                obj.entryzhuanzheng = ruzhishijian - relativedelta(months=-1)
            if form.cleaned_data['zhuanfujing']:
                zhuanfushijian = form.cleaned_data['zhuanfujing']
                obj.fujingzhuanzheng = zhuanfushijian - relativedelta(months=-2)
            obj.sex = xingbie
            obj.birthday = shengri
            obj.zodiac = shengxiao
            obj.constellation = xingzuo
        obj.save()

    # 不可修改字段
    def get_readonly_fields(self, request, obj=None):
        fields = []
        current_user_set = request.user
        if request.user.is_superuser:
            return fields
        elif current_user_set.groups.all():
            current_group_set = Group.objects.get(user=current_user_set)
            if '人事管理' in str(current_group_set):
                fields = ['user', 'sex', 'birthday', 'constellation', 'jiguan', 'zodiac', 'is_delete']
                return fields
            elif '普通用户' in str(current_group_set):
                fields = ['user', 'sex', 'birthday', 'constellation', 'jiguan', 'zodiac',
                          'entry', 'entryzhuanzheng', 'zhuanfujing', 'fujingzhuanzheng', 'quit', 'category',
                          'gangweitype', 'veteran',
                          'gangweiname', 'dadui', 'zhongdui',
                          'jiediao', 'bianzhi', 'is_delete']
                return fields


admin.site.register(UserInformation, UserInformationAdmin)
admin.site.register(PersonalInformation, PersonalinformationAdmin)
