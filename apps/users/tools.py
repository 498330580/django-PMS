# -*- coding: utf-8 -*-
# @Time    : 2020-01-20-0020 16:38
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : tools.py
# @Software: PyCharm

import datetime


class GetInformation(object):
    """根据身份证判断生日、男女、年龄、生肖"""

    def __init__(self, id):
        self.id = id
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        birthday = "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)
        return birthday

    def get_sex(self):
        """男生：1 女生：2"""
        num = int(self.id[16:17])
        if num % 2 == 0:
            return '女'
        else:
            return '男'

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.datetime.now() + datetime.timedelta(days=1))
        year = now.year
        month = now.month
        day = now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_zodiac(self):
        """通过身份证判断生肖"""
        return '猴鸡狗猪鼠牛虎兔龙蛇马羊'[self.birth_year % 12]

    def get_constellation(self):
        n = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
             '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
        d = (
            (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
            (12, 23))
        return n[len(list(filter(lambda y: y <= (self.birth_month, self.birth_day), d))) % 12]

    def get_6(self):
        """通过身份证获取前三位籍贯编码"""
        return self.id[:6]
