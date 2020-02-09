# -*- coding: utf-8 -*-
# @Time    : 2019-09-12-0012 15:35
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : import_classification_data.py
# @Software: PyCharm

import os
import sys

import pandas as pd

# import datetime
# from dateutil.relativedelta import relativedelta

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PMS.settings")

import django

django.setup()

from db_tools.data.classification_data import *
from apps.users.models import *
from django.contrib.auth.models import Group
from apps.users.admin import GetInformation

# print('写入人员类别')
# # 写入人员类别
# for Category in CategoryType_data:
#     if not CategoryType.objects.filter(name=Category['name']):
#         category = CategoryType()
#         category.name = Category['name']
#         category.introduce = Category['introduce']
#         category.index = Category['index']
#         category.save()
# print('写入人员类别结束')


print('写入人员类别')
# 写入人员类别
for Category in CategoryType_data:
    if not CategoryType.objects.filter(name=Category['name']):
        fenzhu = CategoryType()
        fenzhu.name = Category['name']
        fenzhu.desc = Category['introduce']
        fenzhu.index = Category['index']
        fenzhu.category_type = Category['category_type']
        fenzhu.save()
        for i in Category['data']:
            fenzhu_two = CategoryType()
            fenzhu_two.parent_category = fenzhu
            fenzhu_two.name = i['name']
            fenzhu_two.desc = i['introduce']
            fenzhu_two.index = i['index']
            fenzhu_two.category_type = i['category_type']
            fenzhu_two.save()
            for ii in i['data']:
                fenzhu_3 = CategoryType()
                fenzhu_3.parent_category = fenzhu_two
                fenzhu_3.name = ii['name']
                fenzhu_3.desc = ii['introduce']
                fenzhu_3.index = ii['index']
                fenzhu_3.category_type = ii['category_type']
                fenzhu_3.save()
    else:
        pass
        # fenzhu = CategoryType.objects.get(name=Category['name'])
        # for i in Category['data']:
        #     if not CategoryType.objects.filter(name=i['name']):
        #         fenzhu_two = CategoryType()
        #         fenzhu_two.parent_category = fenzhu
        #         fenzhu_two.name = i['name']
        #         fenzhu_two.desc = i['introduce']
        #         fenzhu_two.index = i['index']
        #         fenzhu_two.category_type = i['category_type']
        #         fenzhu_two.save()
print('写入人员类别结束')

print('写入退伍军人类别')
# 写入退伍军人类别
for Demobilized in DemobilizedType_data:
    if not DemobilizedType.objects.filter(name=Demobilized['name']):
        demobilized = DemobilizedType()
        demobilized.name = Demobilized['name']
        demobilized.introduce = Demobilized['introduce']
        demobilized.index = Demobilized['index']
        demobilized.save()
print('写入退伍军人类别结束')

print('写入驾照类别')
# 写入驾照类别
for DrivingLicense in DrivingLicenseType_data:
    if not DrivingLicenseType.objects.filter(name=DrivingLicense['name']):
        drivingLicense = DrivingLicenseType()
        drivingLicense.name = DrivingLicense['name']
        drivingLicense.introduce = DrivingLicense['introduce']
        drivingLicense.index = DrivingLicense['index']
        drivingLicense.save()
print('写入驾照类别结束')

# 写入分组
for DaduiZhongdui in DaduiZhongduiType_data:
    if not DaduiZhongduiType.objects.filter(name=DaduiZhongdui['name']):
        fenzhu = DaduiZhongduiType()
        fenzhu.name = DaduiZhongdui['name']
        fenzhu.desc = DaduiZhongdui['introduce']
        fenzhu.index = DaduiZhongdui['index']
        fenzhu.category_type = DaduiZhongdui['category_type']
        fenzhu.save()
        for i in DaduiZhongdui['data']:
            fenzhu_two = DaduiZhongduiType()
            fenzhu_two.parent_category = fenzhu
            fenzhu_two.name = i['name']
            fenzhu_two.desc = i['introduce']
            fenzhu_two.index = i['index']
            fenzhu_two.category_type = i['category_type']
            fenzhu_two.save()
    else:
        fenzhu = DaduiZhongduiType.objects.get(name=DaduiZhongdui['name'])
        for i in DaduiZhongdui['data']:
            if not DaduiZhongduiType.objects.filter(name=i['name']):
                fenzhu_two = DaduiZhongduiType()
                fenzhu_two.parent_category = fenzhu
                fenzhu_two.name = i['name']
                fenzhu_two.desc = i['introduce']
                fenzhu_two.index = i['index']
                fenzhu_two.category_type = i['category_type']
                fenzhu_two.save()

# # 写入大队类别
# for DaDui in DaDuiType_data:
#     if not DaDuiType.objects.filter(name=DaDui['name']):
#         dadui = DaDuiType()
#         dadui.name = DaDui['name']
#         dadui.introduce = DaDui['introduce']
#         dadui.index = DaDui['index']
#         dadui.save()

# # 写入中队（小组）类别
# for ZhongDui in ZhongDuiType_data:
#     if not ZhongDuiType.objects.filter(name=ZhongDui['name']):
#         zhongdui = ZhongDuiType()
#         zhongdui.name = ZhongDui['name']
#         zhongdui.introduce = ZhongDui['introduce']
#         zhongdui.index = ZhongDui['index']
#         zhongdui.save()

# 写入编制位置
for organization in Organization_data:
    if not Organization.objects.filter(name=organization['name']):
        bianzhi = Organization()
        bianzhi.name = organization['name']
        bianzhi.introduce = organization['introduce']
        bianzhi.index = organization['index']
        bianzhi.save()

# 写入借调位置
for borrow in Borrow_data:
    if not Borrow.objects.filter(name=borrow['name']):
        jiediao = Borrow()
        jiediao.name = borrow['name']
        jiediao.introduce = borrow['introduce']
        jiediao.index = borrow['index']
        jiediao.save()

# 写入经济状态
for economics in Economics_data:
    if not Economics.objects.filter(name=economics['name']):
        economics_tmp = Economics()
        economics_tmp.name = economics['name']
        economics_tmp.introduce = economics['introduce']
        economics_tmp.index = economics['index']
        economics_tmp.save()

print('写入经济来源')
# 写入经济来源
for sources in Sources_data:
    if not Sources.objects.filter(name=sources['name']):
        Sources_tmp = Sources()
        Sources_tmp.name = sources['name']
        Sources_tmp.introduce = sources['introduce']
        Sources_tmp.index = sources['index']
        Sources_tmp.save()
print('写入经济来源结束')

# 写入学历类型
for Education in EducationType_data:
    if not EducationType.objects.filter(name=Education['name']):
        education = EducationType()
        education.name = Education['name']
        education.introduce = Education['introduce']
        education.index = Education['index']
        education.save()

# 写入学位类型
for AcademicDegree in AcademicDegreeType_data:
    if not AcademicDegreeType.objects.filter(name=AcademicDegree['name']):
        academicDegree = AcademicDegreeType()
        academicDegree.name = AcademicDegree['name']
        academicDegree.introduce = AcademicDegree['introduce']
        academicDegree.index = AcademicDegree['index']
        academicDegree.save()

# 写入车辆类别
for Car_tmp in CarType_data:
    if not CarType.objects.filter(name=Car_tmp['name']):
        car = CarType()
        car.name = Car_tmp['name']
        car.introduce = Car_tmp['introduce']
        car.index = Car_tmp['index']
        car.save()

# # 写入岗位类别
# for Post in PostType_data:
#     if not PostType.objects.filter(name=Post['name']):
#         post = PostType()
#         post.name = Post['name']
#         post.introduce = Post['introduce']
#         post.index = Post['index']
#         post.save()
#
# # 写入岗位名称
# for Post in PostName_data:
#     if not PostName.objects.filter(name=Post['name']):
#         post = PostName()
#         post.name = Post['name']
#         post.introduce = Post['introduce']
#         post.index = Post['index']
#         post.save()

# 写入学历说明
for data in XueLiInformation_data:
    if not XueLiInformation.objects.filter(name=data['name']):
        data_obj = XueLiInformation()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()

# 写入人员现状
for data in RenYuanXianZhuang_data:
    if not RenYuanXianZhuang.objects.filter(name=data['name']):
        data_obj = RenYuanXianZhuang()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()

# 写入身份归类
for data in ShenFenGuiLei_data:
    if not ShenFenGuiLei.objects.filter(name=data['name']):
        data_obj = ShenFenGuiLei()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()

# 写入称谓
for data in ChengWei_data:
    if not ChengWei.objects.filter(name=data['name']):
        data_obj = ChengWei()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()

# 写入体检结果
for data in TiJianJieGuo_data:
    if not TiJianJieGuo.objects.filter(name=data['name']):
        data_obj = TiJianJieGuo()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()

print('写入体检年份')
# 写入体检年份
for data in Year_data:
    if not Year.objects.filter(year=data):
        data_obj = Year()
        data_obj.year = data
        data_obj.save()
print('写入体检年份结束')

print('写入地址编码')
# 写入地址编码
data = pd.read_excel('./data/籍贯表.xls')
for index, row in data.iterrows():
    if not DiZhi.objects.filter(dizhi_id=row['编号']):
        print(row['编号'], row['地区'])
        data_obj = DiZhi()
        data_obj.dizhi_id = row['编号']
        data_obj.jiguan = row['地区']
        data_obj.save()
print('写入地址编码结束')

print('写入政治面貌')
# 写入政治面貌
for data in Politics_data:
    if not Politics.objects.filter(name=data['name']):
        data_obj = Politics()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()
print('写入政治面貌结束')

print('写入户籍类型')
# 写入政治面貌
for data in PermanentType_data:
    if not PermanentType.objects.filter(name=data['name']):
        data_obj = PermanentType()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()
print('写入户籍类型结束')

print('写入婚姻状况')
# 写入政治面貌
for data in Marriage_data:
    if not Marriage.objects.filter(name=data['name']):
        data_obj = Marriage()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()
print('写入婚姻状况结束')

print('写入人员状态')
# 写入人员状态
for data in ZhuangTai_data:
    if not ZhuangTai.objects.filter(name=data['name']):
        data_obj = ZhuangTai()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()
print('写入人员状态结束')

print('写入用工信息')
# 写入人员状态
for data in YongGong_data:
    if not YongGongType.objects.filter(name=data['name']):
        data_obj = YongGongType()
        data_obj.name = data['name']
        data_obj.introduce = data['introduce']
        data_obj.index = data['index']
        data_obj.save()
print('写入用工信息结束')

# print('写入用户组与用户角色开始')
# for role in [{'内勤': '所有'}, {'大队长': '大队'}, {'中队长': '中队'}, {'队员': '个人'}]:
#     if not Group.objects.filter(name=list(role.keys())[0]) and not Role.objects.filter(name=list(role.keys())[0]):
#         '''用户角色与用户组都未创建'''
#         Role.objects.create(name=list(role.keys())[0], ranges=list(role.values())[0])
#     elif not Group.objects.filter(name=list(role.keys())[0]) and Role.objects.filter(name=list(role.keys())[0]):
#         '''角色存在，用户组不存在的情况'''
#         group = Group.objects.create(name=list(role.keys())[0])
#         role = Role.objects.get(name=list(role.keys())[0])
#         role.group = group
#         role.save()
#     elif Group.objects.filter(name=list(role.keys())[0]) and not Role.objects.filter(name=list(role.keys())[0]):
#         '''用户组存在，角色不存在的情况'''
#         Role.objects.create(name=list(role.keys())[0], ranges=list(role.values())[0])
#     else:
#         print('用户组(角色)： %s 已存在' % list(role.keys())[0])
# print('写入用户组与用户角色结束')

# '''
# print('写入数据')
# # 写入数据
# data = pd.read_excel('./data/大队人员统计表（2019.09.17）.xls')
# data.fillna(0, inplace=True)
# for index, row in data.iterrows():
#     if not UserInformation.objects.filter(username=row['身份证号码'].upper()):
#         # 验证账户是否存在
#         UserInformation.objects.create_user(username=row['身份证号码'].upper(), password='Tjzd68316070.')
#         user = UserInformation.objects.get(username=row['身份证号码'].upper())
#         # user.is_staff = True      # 可以登录后台
#         # user.is_active = True       # 人员有效
#         user.last_name = row['姓名'][0]
#         user.first_name = row['姓名'][1:]
#         group = Group.objects.get(name='队员')
#         user.groups.add(group)
#         user.save()
#         if not Role.objects.filter(users__username=user, name='队员'):
#             Role.objects.get(name='队员').users.add(user)
# 
#         if not PersonalInformation.objects.filter(idnumber=row['身份证号码'].upper()):
#             # 验证个人信息是否存在
#             print('写入:{}-{}'.format(row['身份证号码'].upper(), row['姓名']))
#             data_obj = PersonalInformation()
#             data_obj.user = user
#             data_obj.name = row['姓名']
#             data_obj.named = row['曾用名']
#             data_obj.idnumber = row['身份证号码'].upper()
#             data_obj.sex = GetInformation(row['身份证号码'].upper()).get_sex()
#             data_obj.birthday = datetime.date(
#                 *map(int, (GetInformation(row['身份证号码'].upper()).get_birthday()).split('-')))
#             data_obj.zodiac = GetInformation(row['身份证号码'].upper()).get_zodiac()
#             data_obj.constellation = GetInformation(row['身份证号码'].upper()).get_constellation()
#             data_obj.jiguan = DiZhi.objects.get(dizhi_id=GetInformation(row['身份证号码'].upper()).get_6())
#             data_obj.permanent = row['户籍地址']
#             data_obj.permanenttype = row['户籍类别']
#             data_obj.home = row['现居地']
#             data_obj.hobby = row['爱好、特长']
#             data_obj.politics = row['政治面貌']
#             if row['入党/团时间'] != '无':
#                 data_obj.politicstime = row['入党/团时间']
#             data_obj.category = CategoryType.objects.get(name=row['人员类别'])
#             data_obj.veteran = DemobilizedType.objects.get(name=row['退伍军人'])
#             data_obj.marriage = row['婚否']
#             data_obj.drivinglicense = DrivingLicenseType.objects.get(name=row['驾照'])
#             data_obj.entry = row['入职时间']
#             data_obj.entryzhuanzheng = row['入职时间'] - relativedelta(months=-1)
#             if row['转辅时间'] != '未转':
#                 data_obj.zhuanfujing = row['转辅时间']
#                 data_obj.fujingzhuanzheng = row['转辅时间'] - relativedelta(months=-2)
#             data_obj.mobile = row['联系电话']
#             if row['离职时间'] != '未离职':
#                 data_obj.quit = row['离职时间']
#             data_obj.dadui = DaDuiType.objects.get(name=row['所属大队'])
#             if row['所属中队'] != '未分配':
#                 data_obj.zhongdui = ZhongDuiType.objects.get(name=row['所属中队'])
#                 data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'], sub_cat__name=row['所属大队'])
#             else:
#                 data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
#             data_obj.jiediao = Borrow.objects.get(name=row['是否借调'])
#             data_obj.bianzhi = Organization.objects.get(name=row['编制位置'])
#             data_obj.economics = Economics.objects.get(name=row['家庭经济状况'])
#             data_obj.sources = Sources.objects.get(name=row['家庭经济来源'])
#             data_obj.nation = '汉族'
#             if row['人员类别'] == '勤务辅警':
#                 data_obj.gangweitype = PostType.objects.get(name='治安辅助')
#                 data_obj.gangweiname = PostName.objects.get(name='维稳勤务岗')
#             elif row['人员类别'] == '协勤队员':
#                 data_obj.gangweitype = PostType.objects.get(name='维稳协勤')
#                 data_obj.gangweiname = PostName.objects.get(name='维稳协勤岗')
#             elif row['人员类别'] == '特勤队员':
#                 data_obj.gangweitype = PostType.objects.get(name='看护特勤')
#                 data_obj.gangweiname = PostName.objects.get(name='看护特勤岗')
#             else:
#                 data_obj.gangweitype = PostType.objects.get(name='警务保障')
#                 data_obj.gangweiname = PostName.objects.get(name='后勤服务岗')
#             data_obj.save()
# 
#             measureinformation = MeasureInformation()
#             measureinformation.name = data_obj
#             measureinformation.year = Year.objects.get(year=2019)
#             measureinformation.shengao = row['身高(CM)']
#             measureinformation.tizhong = row['体重(KG)']
#             measureinformation.xiongwei = row['净胸围(CM)']
#             measureinformation.jiankuan = row['肩宽(CM)']
#             measureinformation.xiuchang = row['袖长(CM)']
#             measureinformation.yaowei = row['平时腰围(CM)']
#             measureinformation.tunwei = row['臀净围(CM)']
#             measureinformation.duwei = row['肚围(CM)']
#             measureinformation.kuchang = row['裤长(CM)']
#             measureinformation.datuiwei = row['大腿围(CM)']
#             measureinformation.maowei = row['帽围(CM)']
#             measureinformation.xiezi = row['鞋子(CM)']
#             measureinformation.save()
# 
#             if row['车牌号码'] != '无':
#                 car = Car()
#                 car.name = data_obj
#                 car.vehicle = row['车牌号码']
#                 car.vehiclecategory = CarType.objects.get(name=row['车辆类别'])
#                 car.save()
#         else:
#             if not PersonalInformation.objects.filter(user=user):
#                 personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
#                 personalinformation.user = user
#                 personalinformation.save()
#     else:
#         user = UserInformation.objects.get(username=row['身份证号码'].upper())
#         group = Group.objects.get(name='队员')
#         user.groups.add(group)
#         user.save()
#         if not Role.objects.filter(users__username=user, name='队员'):
#             Role.objects.get(name='队员').users.add(user)
#         if not PersonalInformation.objects.filter(idnumber=row['身份证号码'].upper()):
#             print('写入:{}-{}'.format(row['身份证号码'].upper(), row['姓名']))
#             data_obj = PersonalInformation()
#             data_obj.user = user
#             data_obj.name = row['姓名']
#             data_obj.named = row['曾用名']
#             data_obj.idnumber = row['身份证号码'].upper()
#             data_obj.sex = GetInformation(row['身份证号码'].upper()).get_sex()
#             data_obj.birthday = datetime.date(
#                 *map(int, (GetInformation(row['身份证号码'].upper()).get_birthday()).split('-')))
#             data_obj.zodiac = GetInformation(row['身份证号码'].upper()).get_zodiac()
#             data_obj.constellation = GetInformation(row['身份证号码'].upper()).get_constellation()
#             data_obj.jiguan = DiZhi.objects.get(dizhi_id=GetInformation(row['身份证号码'].upper()).get_6())
#             data_obj.permanent = row['户籍地址']
#             data_obj.permanenttype = row['户籍类别']
#             data_obj.home = row['现居地']
#             data_obj.hobby = row['爱好、特长']
#             data_obj.politics = row['政治面貌']
#             if row['入党/团时间'] != '无':
#                 data_obj.politicstime = row['入党/团时间']
#             data_obj.category = CategoryType.objects.get(name=row['人员类别'])
#             data_obj.veteran = DemobilizedType.objects.get(name=row['退伍军人'])
#             data_obj.marriage = row['婚否']
#             data_obj.drivinglicense = DrivingLicenseType.objects.get(name=row['驾照'])
#             data_obj.entry = row['入职时间']
#             data_obj.entryzhuanzheng = row['入职时间'] - relativedelta(months=-1)
#             if row['转辅时间'] != '未转':
#                 data_obj.zhuanfujing = row['转辅时间']
#                 data_obj.fujingzhuanzheng = row['转辅时间'] - relativedelta(months=-2)
#             data_obj.mobile = row['联系电话']
#             if row['离职时间'] != '未离职':
#                 data_obj.quit = row['离职时间']
#             data_obj.dadui = DaDuiType.objects.get(name=row['所属大队'])
#             if row['所属中队'] != '未分配':
#                 data_obj.zhongdui = ZhongDuiType.objects.get(name=row['所属中队'])
#                 data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'], sub_cat__name=row['所属大队'])
#             else:
#                 data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
#             data_obj.jiediao = Borrow.objects.get(name=row['是否借调'])
#             data_obj.bianzhi = Organization.objects.get(name=row['编制位置'])
#             data_obj.economics = Economics.objects.get(name=row['家庭经济状况'])
#             data_obj.sources = Sources.objects.get(name=row['家庭经济来源'])
#             data_obj.nation = '汉族'
#             if row['人员类别'] == '勤务辅警':
#                 data_obj.gangweitype = PostType.objects.get(name='治安辅助')
#                 data_obj.gangweiname = PostName.objects.get(name='维稳勤务岗')
#             elif row['人员类别'] == '协勤队员':
#                 data_obj.gangweitype = PostType.objects.get(name='维稳协勤')
#                 data_obj.gangweiname = PostName.objects.get(name='维稳协勤岗')
#             elif row['人员类别'] == '特勤队员':
#                 data_obj.gangweitype = PostType.objects.get(name='看护特勤')
#                 data_obj.gangweiname = PostName.objects.get(name='看护特勤岗')
#             else:
#                 data_obj.gangweitype = PostType.objects.get(name='警务保障')
#                 data_obj.gangweiname = PostName.objects.get(name='后勤服务岗')
#             data_obj.save()
# 
#             measureinformation = MeasureInformation()
#             measureinformation.name = data_obj
#             measureinformation.year = Year.objects.get(year=2019)
#             measureinformation.shengao = row['身高(CM)']
#             measureinformation.tizhong = row['体重(KG)']
#             measureinformation.xiongwei = row['净胸围(CM)']
#             measureinformation.jiankuan = row['肩宽(CM)']
#             measureinformation.xiuchang = row['袖长(CM)']
#             measureinformation.yaowei = row['平时腰围(CM)']
#             measureinformation.tunwei = row['臀净围(CM)']
#             measureinformation.duwei = row['肚围(CM)']
#             measureinformation.kuchang = row['裤长(CM)']
#             measureinformation.datuiwei = row['大腿围(CM)']
#             measureinformation.maowei = row['帽围(CM)']
#             measureinformation.xiezi = row['鞋子(CM)']
#             measureinformation.save()
# 
#             if row['车牌号码'] != '无':
#                 car = Car()
#                 car.name = data_obj
#                 car.vehicle = row['车牌号码']
#                 car.vehiclecategory = CarType.objects.get(name=row['车辆类别'])
#                 car.save()
#         else:
#             if not PersonalInformation.objects.filter(user=user):
#                 personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
#                 personalinformation.user = user
#                 personalinformation.save()
#             else:
#                 personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
#                 if row['所属中队'] != '未分配':
#                     print(row['所属中队'], row['所属大队'])
#                     d = DaduiZhongduiType.objects.get(name=row['所属大队'])
#                     personalinformation.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'],
#                                                                               parent_category=d.id
#                                                                               )
#                 else:
#                     personalinformation.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
#                 personalinformation.save()
# print("写入数据结束")
# '''

print('写入数据')
# 写入数据(重写大队、中队、小组分类)
data = pd.read_excel('./data/2020.2.4.xls')
data.fillna(0, inplace=True)
for index, row in data.iterrows():
    if not UserInformation.objects.filter(username=row['身份证号码'].upper()):
        # 验证账户是否存在
        UserInformation.objects.create_user(username=row['身份证号码'].upper(), password='Tjzd68316070.')
        user = UserInformation.objects.get(username=row['身份证号码'].upper())
        # user.is_staff = True      # 可以登录后台
        # user.is_active = True       # 人员有效
        user.last_name = row['姓名'][0]
        user.first_name = row['姓名'][1:]
        # group = Group.objects.get(name='队员')
        # user.groups.add(group)
        user.save()
        # if not Role.objects.filter(users__username=user, name='队员'):
        #     Role.objects.get(name='队员').users.add(user)

        if not PersonalInformation.objects.filter(idnumber=row['身份证号码'].upper()):
            # 验证个人信息是否存在
            print('写入:{}-{}'.format(row['身份证号码'].upper(), row['姓名']))
            data_obj = PersonalInformation()
            data_obj.user = user
            data_obj.idfj = row['辅警编号']
            data_obj.name = row['姓名']
            data_obj.named = row['曾用名']
            data_obj.idnumber = row['身份证号码'].upper()
            data_obj.sex = GetInformation(row['身份证号码'].upper()).get_sex()
            data_obj.birthday = datetime.date(
                *map(int, (GetInformation(row['身份证号码'].upper()).get_birthday()).split('-')))
            data_obj.zodiac = GetInformation(row['身份证号码'].upper()).get_zodiac()
            data_obj.constellation = GetInformation(row['身份证号码'].upper()).get_constellation()
            data_obj.jiguan = DiZhi.objects.get(dizhi_id=GetInformation(row['身份证号码'].upper()).get_6())
            data_obj.permanent = row['户籍地址']
            # data_obj.permanenttype = row['户籍类别']
            data_obj.permanenttype = PermanentType.objects.get(name=row['户籍类别'])
            data_obj.home = row['现居地']
            data_obj.hobby = row['爱好、特长']
            # data_obj.politics = row['政治面貌']
            # if row['入党/团时间'] != '无':
            #     """判断并写入入党团时间"""
            #     data_obj.politicstime = row['入党/团时间']
            # data_obj.category = CategoryType.objects.get(name=row['人员类别'])
            data_obj.veteran = DemobilizedType.objects.get(name=row['退伍军人'])
            # data_obj.marriage = row['婚否']
            data_obj.marriage = Marriage.objects.get(name=row['婚否'])
            data_obj.drivinglicense = DrivingLicenseType.objects.get(name=row['驾照'])
            # data_obj.entry = row['入职时间']
            # data_obj.entryzhuanzheng = row['入职时间'] - relativedelta(months=-1)
            # if row['转辅时间'] != '未转':
            #     """判断并写入转辅警的时间"""
            #     data_obj.zhuanfujing = row['转辅时间']
            #     data_obj.fujingzhuanzheng = row['转辅时间'] - relativedelta(months=-2)
            data_obj.mobile = row['联系电话']
            # if row['离职时间'] != '未离职':
            #     """判断并写入离职时间"""
            #     data_obj.quit = row['离职时间']
            # dadui = DaduiZhongduiType.objects.get(name=row['所属大队'])
            data_obj.dadui = DaduiZhongduiType.objects.get(name=row['所属大队'])
            if row['所属中队'] != '未分配':
                """写入中队信息"""
                data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'], parent_category__name=row['所属大队'])
                # data_obj.fenzu = dadui.sub_cat.filter(name=row['所属中队'])[0]
            else:
                data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
            data_obj.jiediao = Borrow.objects.get(name=row['是否借调'])
            data_obj.bianzhi = Organization.objects.get(name=row['编制位置'])
            data_obj.economics = Economics.objects.get(name=row['家庭经济状况'])
            data_obj.sources = Sources.objects.get(name=row['家庭经济来源'])
            data_obj.nation = '汉族'
            # if row['人员类别'] == '勤务辅警':
            #     data_obj.gangweitype = PostType.objects.get(name='治安辅助')
            #     data_obj.gangweiname = PostName.objects.get(name='维稳勤务岗')
            # elif row['人员类别'] == '协勤队员':
            #     data_obj.gangweitype = PostType.objects.get(name='维稳协勤')
            #     data_obj.gangweiname = PostName.objects.get(name='维稳协勤岗')
            # elif row['人员类别'] == '特勤队员':
            #     data_obj.gangweitype = PostType.objects.get(name='看护特勤')
            #     data_obj.gangweiname = PostName.objects.get(name='看护特勤岗')
            # else:
            #     data_obj.gangweitype = PostType.objects.get(name='警务保障')
            #     data_obj.gangweiname = PostName.objects.get(name='后勤服务岗')
            data_obj.save()

            # 写入党团关系
            dangtuan = DangTuan()
            dangtuan.name = data_obj
            dangtuan.politics = Politics.objects.get(name=row['政治面貌'])
            dangtuan.save()

            # 写入履历信息
            lvli = Lvli()
            lvli.name = data_obj
            lvli.remarks = '重庆市北碚区保安服务有限公司派遣'
            if row['人员类别'] == '勤务辅警':
                if row['入职时间'] == row['转辅时间']:
                    lvli.start = row['入职时间']
                    lvli.shenfenguilei = ShenFenGuiLei.objects.get(name=row['人员类别'])
                else:
                    # 写入辅警信息
                    lvli.start = row['转辅时间']
                    lvli.shenfenguilei = ShenFenGuiLei.objects.get(name='勤务辅警')
                    # 写入协勤信息
                    lvli2 = Lvli()
                    lvli2.name = data_obj
                    lvli2.name = data_obj
                    lvli2.remarks = '重庆市北碚区保安服务有限公司派遣'
                    lvli2.start = row['入职时间']
                    lvli2.end = row['转辅时间']
                    lvli2.shenfenguilei = ShenFenGuiLei.objects.get(name='协勤队员')
                    lvli2.save()
            else:
                lvli.start = row['入职时间']
                lvli.shenfenguilei = ShenFenGuiLei.objects.get(name=row['人员类别'])
            if row['离职时间'] != '未离职':
                '''已离职人员写入离职时间'''
                lvli.end = row['离职时间']
            lvli.save()

            # 写入用工信息
            yonggong = YongGong()
            yonggong.name = data_obj
            yonggong.zhuangtai = ZhuangTai.objects.get(name='在岗')
            yonggong.yonggongtype = YongGongType.objects.get(name='劳务派遣')
            if row['人员类别'] == '勤务辅警':
                if row['入职时间'] == row['转辅时间']:
                    yonggong.start = row['入职时间']
                    yonggong.hetong_time = row['入职时间']
                    yonggong.shixiqi = 2
                    yonggong.hetong = 2
                    yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                    yonggong.gangweitype = CategoryType.objects.get(name='治安辅助')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳勤务岗')
                else:
                    # 写入辅警信息
                    yonggong.start = row['转辅时间']
                    yonggong.hetong_time = row['转辅时间']
                    yonggong.shixiqi = 2
                    yonggong.hetong = 2
                    yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                    yonggong.gangweitype = CategoryType.objects.get(name='治安辅助')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳勤务岗')
                    # 写入协勤信息
                    yonggong2 = YongGong()
                    yonggong2.name = data_obj
                    yonggong2.start = row['入职时间']
                    yonggong2.hetong_time = row['入职时间']
                    yonggong2.shixiqi = 1
                    yonggong2.hetong = 1
                    yonggong2.zhuangtai = ZhuangTai.objects.get(name='转辅')
                    yonggong2.end = row['转辅时间']
                    yonggong2.yonggongtype = YongGongType.objects.get(name='劳务派遣')
                    yonggong2.shenfenguilei = CategoryType.objects.get(name='协勤队员')
                    yonggong2.gangweitype = CategoryType.objects.get(name='维稳协勤')
                    yonggong2.gangweiname = CategoryType.objects.get(name='维稳协勤岗')
                    yonggong2.save()

            else:
                yonggong.start = row['入职时间']
                yonggong.hetong_time = row['入职时间']
                yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                yonggong.shixiqi = 1
                yonggong.hetong = 1
                if row['人员类别'] == '协勤队员':
                    yonggong.gangweitype = CategoryType.objects.get(name='维稳协勤')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳协勤岗')
                elif row['人员类别'] == '护卫队员':
                    yonggong.gangweitype = CategoryType.objects.get(name='护卫特勤')
                    yonggong.gangweiname = CategoryType.objects.get(name='护卫特勤岗')
                else:
                    yonggong.gangweitype = CategoryType.objects.get(name='警务保障')
                    yonggong.gangweiname = CategoryType.objects.get(name='警务保障岗')
            if row['离职时间'] != '未离职':
                '''已离职人员写入离职时间'''
                yonggong.end = row['离职时间']
            yonggong.save()

            # 写入个人量体信息
            measureinformation = MeasureInformation()
            measureinformation.name = data_obj
            measureinformation.year = Year.objects.get(year=2019)
            measureinformation.shengao = row['身高(CM)']
            measureinformation.tizhong = row['体重(KG)']
            measureinformation.xiongwei = row['净胸围(CM)']
            measureinformation.jiankuan = row['肩宽(CM)']
            measureinformation.xiuchang = row['袖长(CM)']
            measureinformation.yaowei = row['平时腰围(CM)']
            measureinformation.tunwei = row['臀净围(CM)']
            measureinformation.duwei = row['肚围(CM)']
            measureinformation.kuchang = row['裤长(CM)']
            measureinformation.datuiwei = row['大腿围(CM)']
            measureinformation.maowei = row['帽围(CM)']
            measureinformation.xiezi = row['鞋子(CM)']
            measureinformation.save()

            if row['车牌号码'] != '无':
                car = Car()
                car.name = data_obj
                car.vehicle = row['车牌号码']
                car.vehiclecategory = CarType.objects.get(name=row['车辆类别'])
                car.save()
        else:
            if not PersonalInformation.objects.filter(user=user):
                personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
                personalinformation.user = user
                personalinformation.save()
    else:
        user = UserInformation.objects.get(username=row['身份证号码'].upper())
        # group = Group.objects.get(name='队员')
        # user.groups.add(group)
        user.save()
        # if not Role.objects.filter(users__username=user, name='队员'):
        #     Role.objects.get(name='队员').users.add(user)
        if not PersonalInformation.objects.filter(idnumber=row['身份证号码'].upper()):
            print('写入:{}-{}'.format(row['身份证号码'].upper(), row['姓名']))
            data_obj = PersonalInformation()
            data_obj.user = user
            data_obj.idfj = row['辅警编号']
            data_obj.name = row['姓名']
            data_obj.named = row['曾用名']
            data_obj.idnumber = row['身份证号码'].upper()
            data_obj.sex = GetInformation(row['身份证号码'].upper()).get_sex()
            data_obj.birthday = datetime.date(
                *map(int, (GetInformation(row['身份证号码'].upper()).get_birthday()).split('-')))
            data_obj.zodiac = GetInformation(row['身份证号码'].upper()).get_zodiac()
            data_obj.constellation = GetInformation(row['身份证号码'].upper()).get_constellation()
            data_obj.jiguan = DiZhi.objects.get(dizhi_id=GetInformation(row['身份证号码'].upper()).get_6())
            data_obj.permanent = row['户籍地址']
            # data_obj.permanenttype = row['户籍类别']
            data_obj.permanenttype = PermanentType.objects.get(name=row['户籍类别'])
            data_obj.home = row['现居地']
            data_obj.hobby = row['爱好、特长']
            # data_obj.politics = row['政治面貌']
            # if row['入党/团时间'] != '无':
            #     """判断并写入入党团时间"""
            #     data_obj.politicstime = row['入党/团时间']
            # data_obj.category = CategoryType.objects.get(name=row['人员类别'])
            data_obj.veteran = DemobilizedType.objects.get(name=row['退伍军人'])
            # data_obj.marriage = row['婚否']
            data_obj.marriage = Marriage.objects.get(name=row['婚否'])
            data_obj.drivinglicense = DrivingLicenseType.objects.get(name=row['驾照'])
            # data_obj.entry = row['入职时间']
            # data_obj.entryzhuanzheng = row['入职时间'] - relativedelta(months=-1)
            # if row['转辅时间'] != '未转':
            #     """判断并写入转辅警的时间"""
            #     data_obj.zhuanfujing = row['转辅时间']
            #     data_obj.fujingzhuanzheng = row['转辅时间'] - relativedelta(months=-2)
            data_obj.mobile = row['联系电话']
            # if row['离职时间'] != '未离职':
            #     """判断并写入离职时间"""
            #     data_obj.quit = row['离职时间']
            # dadui = DaduiZhongduiType.objects.get(name=row['所属大队'])
            data_obj.dadui = DaduiZhongduiType.objects.get(name=row['所属大队'])
            if row['所属中队'] != '未分配':
                """写入中队信息"""
                data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'], parent_category__name=row['所属大队'])
                # data_obj.fenzu = dadui.sub_cat.filter(name=row['所属中队'])[0]
            else:
                data_obj.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
            data_obj.jiediao = Borrow.objects.get(name=row['是否借调'])
            data_obj.bianzhi = Organization.objects.get(name=row['编制位置'])
            data_obj.economics = Economics.objects.get(name=row['家庭经济状况'])
            data_obj.sources = Sources.objects.get(name=row['家庭经济来源'])
            data_obj.nation = '汉族'
            # if row['人员类别'] == '勤务辅警':
            #     data_obj.gangweitype = PostType.objects.get(name='治安辅助')
            #     data_obj.gangweiname = PostName.objects.get(name='维稳勤务岗')
            # elif row['人员类别'] == '协勤队员':
            #     data_obj.gangweitype = PostType.objects.get(name='维稳协勤')
            #     data_obj.gangweiname = PostName.objects.get(name='维稳协勤岗')
            # elif row['人员类别'] == '特勤队员':
            #     data_obj.gangweitype = PostType.objects.get(name='看护特勤')
            #     data_obj.gangweiname = PostName.objects.get(name='看护特勤岗')
            # else:
            #     data_obj.gangweitype = PostType.objects.get(name='警务保障')
            #     data_obj.gangweiname = PostName.objects.get(name='后勤服务岗')
            data_obj.save()

            # 写入党团关系
            dangtuan = DangTuan()
            dangtuan.name = data_obj
            dangtuan.politics = Politics.objects.get(name=row['政治面貌'])
            dangtuan.save()

            # 写入履历信息
            lvli = Lvli()
            lvli.name = data_obj
            lvli.remarks = '重庆市北碚区保安服务有限公司派遣'
            if row['人员类别'] == '勤务辅警':
                if row['入职时间'] == row['转辅时间']:
                    lvli.start = row['入职时间']
                    lvli.shenfenguilei = ShenFenGuiLei.objects.get(name=row['人员类别'])
                else:
                    # 写入辅警信息
                    lvli.start = row['转辅时间']
                    lvli.shenfenguilei = ShenFenGuiLei.objects.get(name='勤务辅警')
                    # 写入协勤信息
                    lvli2 = Lvli()
                    lvli2.name = data_obj
                    lvli2.name = data_obj
                    lvli2.remarks = '重庆市北碚区保安服务有限公司派遣'
                    lvli2.start = row['入职时间']
                    lvli2.end = row['转辅时间']
                    lvli2.shenfenguilei = ShenFenGuiLei.objects.get(name='协勤队员')
                    lvli2.save()
            else:
                lvli.start = row['入职时间']
                lvli.shenfenguilei = ShenFenGuiLei.objects.get(name=row['人员类别'])
            if row['离职时间'] != '未离职':
                '''已离职人员写入离职时间'''
                lvli.end = row['离职时间']
            lvli.save()

            # 写入用工信息
            yonggong = YongGong()
            yonggong.name = data_obj
            yonggong.zhuangtai = ZhuangTai.objects.get(name='在岗')
            yonggong.yonggongtype = YongGongType.objects.get(name='劳务派遣')
            if row['人员类别'] == '勤务辅警':
                if row['入职时间'] == row['转辅时间']:
                    yonggong.start = row['入职时间']
                    yonggong.hetong_time = row['入职时间']
                    yonggong.shixiqi = 2
                    yonggong.hetong = 2
                    yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                    yonggong.gangweitype = CategoryType.objects.get(name='治安辅助')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳勤务岗')
                else:
                    # 写入辅警信息
                    yonggong.start = row['转辅时间']
                    yonggong.hetong_time = row['转辅时间']
                    yonggong.shixiqi = 2
                    yonggong.hetong = 2
                    yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                    yonggong.gangweitype = CategoryType.objects.get(name='治安辅助')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳勤务岗')
                    # 写入协勤信息
                    yonggong2 = YongGong()
                    yonggong2.name = data_obj
                    yonggong2.start = row['入职时间']
                    yonggong2.hetong_time = row['入职时间']
                    yonggong2.shixiqi = 1
                    yonggong2.hetong = 1
                    yonggong2.zhuangtai = ZhuangTai.objects.get(name='转辅')
                    yonggong2.end = row['转辅时间']
                    yonggong2.yonggongtype = YongGongType.objects.get(name='劳务派遣')
                    yonggong2.shenfenguilei = CategoryType.objects.get(name='协勤队员')
                    yonggong2.gangweitype = CategoryType.objects.get(name='维稳协勤')
                    yonggong2.gangweiname = CategoryType.objects.get(name='维稳协勤岗')
                    yonggong2.save()

            else:
                yonggong.start = row['入职时间']
                yonggong.hetong_time = row['入职时间']
                yonggong.shenfenguilei = CategoryType.objects.get(name=row['人员类别'])
                yonggong.shixiqi = 1
                yonggong.hetong = 1
                if row['人员类别'] == '协勤队员':
                    yonggong.gangweitype = CategoryType.objects.get(name='维稳协勤')
                    yonggong.gangweiname = CategoryType.objects.get(name='维稳协勤岗')
                elif row['人员类别'] == '护卫队员':
                    yonggong.gangweitype = CategoryType.objects.get(name='护卫特勤')
                    yonggong.gangweiname = CategoryType.objects.get(name='护卫特勤岗')
                else:
                    yonggong.gangweitype = CategoryType.objects.get(name='警务保障')
                    yonggong.gangweiname = CategoryType.objects.get(name='警务保障岗')
            if row['离职时间'] != '未离职':
                '''已离职人员写入离职时间'''
                yonggong.end = row['离职时间']
            yonggong.save()

            # 写入量体信息
            measureinformation = MeasureInformation()
            measureinformation.name = data_obj
            measureinformation.year = Year.objects.get(year=2019)
            measureinformation.shengao = row['身高(CM)']
            measureinformation.tizhong = row['体重(KG)']
            measureinformation.xiongwei = row['净胸围(CM)']
            measureinformation.jiankuan = row['肩宽(CM)']
            measureinformation.xiuchang = row['袖长(CM)']
            measureinformation.yaowei = row['平时腰围(CM)']
            measureinformation.tunwei = row['臀净围(CM)']
            measureinformation.duwei = row['肚围(CM)']
            measureinformation.kuchang = row['裤长(CM)']
            measureinformation.datuiwei = row['大腿围(CM)']
            measureinformation.maowei = row['帽围(CM)']
            measureinformation.xiezi = row['鞋子(CM)']
            measureinformation.save()

            if row['车牌号码'] != '无':
                car = Car()
                car.name = data_obj
                car.vehicle = row['车牌号码']
                car.vehiclecategory = CarType.objects.get(name=row['车辆类别'])
                car.save()
        else:
            if not PersonalInformation.objects.filter(user=user):
                personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
                personalinformation.user = user
                personalinformation.save()
            else:
                """补充信息"""
                personalinformation = PersonalInformation.objects.get(idnumber=row['身份证号码'].upper())
                if row['所属中队'] != '未分配':
                    # d = DaduiZhongduiType.objects.get(name=row['所属大队'])
                    personalinformation.fenzu = DaduiZhongduiType.objects.get(name=row['所属中队'],
                                                                              parent_category__name=row['所属大队']
                                                                              )
                else:
                    personalinformation.fenzu = DaduiZhongduiType.objects.get(name=row['所属大队'])
                personalinformation.save()
print("写入数据结束")
