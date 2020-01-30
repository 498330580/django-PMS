# -*- coding: utf-8 -*-
# @Time    : 2019-09-12-0012 15:34
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : classification_data.py
# @Software: PyCharm

# 人员类别
CategoryType_data = [{'name': '勤务辅警', 'introduce': '已经转为辅警的编制人员。', 'index': 1},
                     {'name': '协勤队员', 'introduce': '未转为辅警的编制人员，原来的特保队员。', 'index': 2},
                     {'name': '特勤队员', 'introduce': '监委的编制人员', 'index': 3},
                     {'name': '工勤人员', 'introduce': '车班', 'index': 4},
                     {'name': '民警', 'introduce': '民警，一般用于设置管理账号', 'index': 5}]

# 退伍军人类别
DemobilizedType_data = [{'name': '未参军', 'introduce': '以前未参军人员。', 'index': 1},
                        {'name': '解放军', 'introduce': '解放军退役人员。', 'index': 2},
                        {'name': '武警', 'introduce': '武警退役人员。', 'index': 3}]

# 驾照类别
DrivingLicenseType_data = [{'name': '未获得', 'introduce': '未获得', 'index': 1},
                           {'name': 'C2', 'introduce': 'C2', 'index': 2},
                           {'name': 'C1', 'introduce': 'C1', 'index': 1},
                           {'name': 'C1D', 'introduce': 'C1D', 'index': 1},
                           {'name': 'C1E', 'introduce': 'C1E', 'index': 1},
                           {'name': 'A1', 'introduce': 'A1', 'index': 5},
                           {'name': 'A1A2', 'introduce': 'A1A2', 'index': 6},
                           {'name': 'B2', 'introduce': 'B2', 'index': 4},
                           {'name': 'B2D', 'introduce': 'B2D', 'index': 4},
                           {'name': 'B2E', 'introduce': 'B2E', 'index': 4},
                           {'name': 'E', 'introduce': 'E', 'index': 3},
                           ]

# 分组类别
DaduiZhongduiType_data = [{'name': '一大队', 'introduce': '一大队', 'index': 110, 'category_type': '大队',
                           'data': [
                               {'name': '一中队', 'introduce': '一中队', 'index': 111, 'category_type': '中队'},
                               {'name': '二中队', 'introduce': '二中队', 'index': 112, 'category_type': '中队'},
                               {'name': '三中队', 'introduce': '三中队', 'index': 113, 'category_type': '中队'},
                               {'name': '四中队', 'introduce': '四中队', 'index': 114, 'category_type': '中队'}
                           ]},
                          {'name': '二大队', 'introduce': '二大队', 'index': 120, 'category_type': '大队',
                           'data': [
                               {'name': '五中队', 'introduce': '五中队', 'index': 121, 'category_type': '中队'},
                               {'name': '六中队', 'introduce': '六中队', 'index': 122, 'category_type': '中队'},
                               {'name': '七中队', 'introduce': '七中队', 'index': 123, 'category_type': '中队'},
                               {'name': '八中队', 'introduce': '八中队', 'index': 124, 'category_type': '中队'}
                           ]},
                          {'name': '三大队', 'introduce': '三大队', 'index': 130, 'category_type': '大队',
                           'data': [
                               {'name': '九中队', 'introduce': '九中队', 'index': 131, 'category_type': '中队'},
                               {'name': '十中队', 'introduce': '十中队', 'index': 132, 'category_type': '中队'},
                               {'name': '十一中队', 'introduce': '十一中队', 'index': 133, 'category_type': '中队'},
                               {'name': '十二中队', 'introduce': '十二中队', 'index': 134, 'category_type': '中队'}
                           ]},
                          {'name': '四大队', 'introduce': '四大队', 'index': 140, 'category_type': '大队',
                           'data': [
                               {'name': '一中队', 'introduce': '一中队', 'index': 141, 'category_type': '中队'},
                               {'name': '二中队', 'introduce': '二中队', 'index': 142, 'category_type': '中队'},
                               {'name': '三中队', 'introduce': '三中队', 'index': 143, 'category_type': '中队'},
                               {'name': '四中队', 'introduce': '四中队', 'index': 144, 'category_type': '中队'},
                               {'name': '五中队', 'introduce': '五中队', 'index': 145, 'category_type': '中队'}
                           ]},
                          {'name': '警保大队', 'introduce': '警保大队', 'index': 100, 'category_type': '大队',
                           'data': [
                               {'name': '应急指挥', 'introduce': '应急指挥', 'index': 101, 'category_type': '小组'},
                               {'name': '应急保障（1）', 'introduce': '应急保障（1）', 'index': 102, 'category_type': '小组'},
                               {'name': '应急保障（2）', 'introduce': '应急保障（2）', 'index': 103, 'category_type': '小组'},
                               {'name': '应急保障（3）', 'introduce': '应急保障（3）', 'index': 104, 'category_type': '小组'},
                               {'name': '门岗', 'introduce': '门岗', 'index': 105, 'category_type': '小组'},
                               {'name': '车班', 'introduce': '车班', 'index': 106, 'category_type': '小组'}
                           ]},
                          ]

# 大队类别
DaDuiType_data = [{'name': '一大队', 'introduce': '一大队', 'index': 1},
                  {'name': '二大队', 'introduce': '二大队', 'index': 2},
                  {'name': '三大队', 'introduce': '三大队', 'index': 3},
                  {'name': '四大队', 'introduce': '四大队', 'index': 4},
                  {'name': '警保大队', 'introduce': '警保大队', 'index': 5},
                  ]

# 中队（小组）类别
ZhongDuiType_data = [{'name': '一中队', 'introduce': '一中队', 'index': 1},
                     {'name': '二中队', 'introduce': '二中队', 'index': 2},
                     {'name': '三中队', 'introduce': '三中队', 'index': 3},
                     {'name': '四中队', 'introduce': '四中队', 'index': 4},
                     {'name': '五中队', 'introduce': '五中队', 'index': 5},
                     {'name': '六中队', 'introduce': '六中队', 'index': 6},
                     {'name': '七中队', 'introduce': '七中队', 'index': 7},
                     {'name': '八中队', 'introduce': '八中队', 'index': 8},
                     {'name': '九中队', 'introduce': '九中队', 'index': 9},
                     {'name': '十中队', 'introduce': '十中队', 'index': 10},
                     {'name': '十一中队', 'introduce': '十一中队', 'index': 11},
                     {'name': '十二中队', 'introduce': '十二中队', 'index': 12},
                     {'name': '应急指挥', 'introduce': '应急指挥', 'index': 13},
                     {'name': '应急保障（1）', 'introduce': '应急保障（1）', 'index': 14},
                     {'name': '应急保障（2）', 'introduce': '应急保障（2）', 'index': 15},
                     {'name': '应急保障（3）', 'introduce': '应急保障（3）', 'index': 16},
                     {'name': '门岗', 'introduce': '门岗', 'index': 17},
                     ]

# 编制位置
Organization_data = [{'name': '特警支队', 'introduce': '本单位编制', 'index': 1},
                     {'name': '警保处', 'introduce': '警保处', 'index': 2},
                     {'name': '监委', 'introduce': '监委', 'index': 3},
                     ]

# 借调位置
Borrow_data = [{'name': '未借调', 'introduce': '未借调', 'index': 1},
               {'name': '交巡警', 'introduce': '交巡警', 'index': 2},
               {'name': '警保处', 'introduce': '警保处', 'index': 3},
               {'name': '指挥中心', 'introduce': '指挥中心', 'index': 4},
               {'name': '特警支队（工勤）', 'introduce': '编制不在本单位的工勤人员选择', 'index': 5},
               ]

# 经济状态
Economics_data = [{'name': '一般', 'introduce': '一般', 'index': 1},
                  {'name': '良好', 'introduce': '良好', 'index': 2},
                  {'name': '贫困', 'introduce': '贫困', 'index': 3},
                  {'name': '不清', 'introduce': '人员并未上报经济状态', 'index': 4},
                  ]

# 经济来源
Sources_data = [{'name': '工资', 'introduce': '工资', 'index': 1},
                {'name': '务工', 'introduce': '务工', 'index': 2},
                {'name': '务农', 'introduce': '务农', 'index': 3},
                {'name': '经商', 'introduce': '经商', 'index': 4},
                {'name': '不清', 'introduce': '人员并未上报经济来源', 'index': 5},
                ]

# 学历类型
EducationType_data = [{'name': '小学', 'introduce': '小学', 'index': 1},
                      {'name': '初中', 'introduce': '初中', 'index': 2},
                      {'name': '高中', 'introduce': '高中', 'index': 3},
                      {'name': '大专', 'introduce': '大专', 'index': 4},
                      {'name': '本科', 'introduce': '本科', 'index': 5},
                      {'name': '职高', 'introduce': '职高', 'index': 6},
                      {'name': '中专', 'introduce': '中专', 'index': 7},
                      ]

# 学位类型
AcademicDegreeType_data = [{'name': '学士学位', 'introduce': '学士学位', 'index': 2},
                           {'name': '硕士学位', 'introduce': '硕士学位', 'index': 3},
                           {'name': '博士学位', 'introduce': '博士学位', 'index': 4},
                           {'name': '未获得学位', 'introduce': '未获得学位', 'index': 1}
                           ]

# 车辆类别
CarType_data = [{'name': '小型汽车', 'introduce': '小型汽车', 'index': 1},
                {'name': '二轮摩托车', 'introduce': '二轮摩托车', 'index': 2},
                ]

# 岗位类别
PostType_data = [{'name': '治安辅助', 'introduce': '治安辅助', 'index': 1},
                 {'name': '警务保障', 'introduce': '警务保障', 'index': 4},
                 {'name': '维稳协勤', 'introduce': '维稳协勤', 'index': 2},
                 {'name': '看护特勤', 'introduce': '看护特勤', 'index': 3}, ]

# 岗位名称
PostName_data = [{'name': '维稳勤务岗', 'introduce': '维稳勤务岗', 'index': 1},
                 {'name': '后勤服务岗', 'introduce': '后勤服务岗', 'index': 4},
                 {'name': '维稳协勤岗', 'introduce': '维稳协勤岗', 'index': 2},
                 {'name': '看护特勤岗', 'introduce': '看护特勤岗', 'index': 3}, ]

# 学历说明
XueLiInformation_data = [{'name': '全日制学历', 'introduce': '全日制学历', 'index': 1},
                         {'name': '在职学历', 'introduce': '在职学历', 'index': 2}, ]

# 人员现状
RenYuanXianZhuang_data = [{'name': '学龄前', 'introduce': '学龄前', 'index': 1},
                          {'name': '上学', 'introduce': '上学', 'index': 2},
                          {'name': '在职', 'introduce': '在职', 'index': 3},
                          {'name': '无业', 'introduce': '无业', 'index': 4},
                          {'name': '腿（离）休', 'introduce': '腿（离）休', 'index': 5},
                          {'name': '去世', 'introduce': '去世', 'index': 6}, ]

# 身份归类
ShenFenGuiLei_data = [{'name': '学龄前儿童', 'introduce': '学龄前儿童', 'index': 1},
                      {'name': '学生', 'introduce': '学生', 'index': 2},
                      {'name': '公务员', 'introduce': '公务员', 'index': 3},
                      {'name': '事业单位职工', 'introduce': '事业单位职工', 'index': 4},
                      {'name': '国有企业职工', 'introduce': '国有企业职工', 'index': 5},
                      {'name': '教师', 'introduce': '教师', 'index': 6},
                      {'name': '军人', 'introduce': '军人', 'index': 7},
                      {'name': '医生', 'introduce': '医生', 'index': 8},
                      {'name': '护士', 'introduce': '护士', 'index': 9},
                      {'name': '私企职工', 'introduce': '私企职工', 'index': 10},
                      {'name': '技术人员', 'introduce': '技术人员', 'index': 11},
                      {'name': '居民', 'introduce': '居民', 'index': 12},
                      {'name': '其他', 'introduce': '其他', 'index': 13}, ]

# 称谓
ChengWei_data = [{'name': '丈夫', 'introduce': '丈夫', 'index': 1},
                 {'name': '妻子', 'introduce': '妻子', 'index': 2},
                 {'name': '儿子', 'introduce': '儿子', 'index': 3},
                 {'name': '女儿', 'introduce': '女儿', 'index': 4},
                 {'name': '父亲', 'introduce': '父亲', 'index': 5},
                 {'name': '母亲', 'introduce': '母亲', 'index': 6},
                 {'name': '岳父', 'introduce': '岳父', 'index': 7},
                 {'name': '公公', 'introduce': '公公', 'index': 8},
                 {'name': '婆婆', 'introduce': '婆婆', 'index': 9},
                 {'name': '哥哥', 'introduce': '哥哥', 'index': 10},
                 {'name': '弟弟', 'introduce': '弟弟', 'index': 11},
                 {'name': '姐姐', 'introduce': '姐姐', 'index': 12},
                 {'name': '儿媳', 'introduce': '儿媳', 'index': 14},
                 {'name': '妹妹', 'introduce': '妹妹', 'index': 13},
                 {'name': '女婿', 'introduce': '女婿', 'index': 15},
                 {'name': '其他近亲', 'introduce': '其他近亲', 'index': 16}, ]

# 体检结果
TiJianJieGuo_data = [{'name': '随访', 'introduce': '随访', 'index': 1},
                     {'name': '良好', 'introduce': '良好', 'index': 2},
                     {'name': '健康', 'introduce': '健康', 'index': 3}, ]

# 体检年份
Year_data = [2019, 2020]
