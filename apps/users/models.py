# Create your models here.
# from django.contrib.auth.models import Group
import datetime
from dateutil.relativedelta import relativedelta
from classification.models import *

from django.db import models
from django.contrib.auth.models import AbstractUser

from .tools import GetInformation

NATION = (('汉族', '汉族'), ('壮族', '壮族'), ('满族', '满族'), ('回族', '回族'), ('苗族', '苗族'), ('维吾尔族', '维吾尔族'), ('土家族', '土家族'),
          ('彝族', '彝族'), ('蒙古族', '蒙古族'), ('藏族', '藏族'), ('布依族', '布依族'), ('侗族', '侗族'), ('瑶族', '瑶族'), ('朝鲜族', '朝鲜族'),
          ('白族', '白族'), ('哈尼族', '哈尼族'), ('哈萨克族', '哈萨克族'), ('黎族', '黎族'), ('傣族', '傣族'), ('畲族', '畲族'), ('傈僳族', '傈僳族'),
          ('仡佬族', '仡佬族'), ('东乡族', '东乡族'), ('高山族', '高山族'), ('拉祜族', '拉祜族'), ('水族', '水族'), ('佤族', '佤族'),
          ('纳西族', '纳西族'),
          ('羌族', '羌族'), ('土族', '土族'), ('仫佬族', '仫佬族'), ('锡伯族', '锡伯族'), ('柯尔克孜族', '柯尔克孜族'), ('达斡尔族', '达斡尔族'),
          ('景颇族', '景颇族'),
          ('毛南族', '毛南族'), ('撒拉族', '撒拉族'), ('布朗族', '布朗族'), ('塔吉克族', '塔吉克族'), ('阿昌族', '阿昌族'), ('普米族', '普米族'),
          ('鄂温克族', '鄂温克族'),
          ('怒族', '怒族'), ('京族', '京族'), ('基诺族', '基诺族'), ('德昂族', '德昂族'), ('保安族', '保安族'), ('俄罗斯族', '俄罗斯族'),
          ('裕固族', '裕固族'),
          ('乌孜别克族', '乌孜别克族'), ('门巴族', '门巴族'), ('鄂伦春族', '鄂伦春族'), ('独龙族', '独龙族'), ('塔塔尔族', '塔塔尔族'), ('赫哲族', '赫哲族'),
          ('珞巴族', '珞巴族'))


'''
# # 角色模型
# class Group(G):
#     ranges_fenzu = models.ManyToManyField(DaduiZhongduiType, verbose_name='权限范围', help_text='角色控制数据的权限范围', blank=True)
#     # group = models.OneToOneField(Group, verbose_name='用户组', help_text='与角色对应的用户组，控制角色权限', on_delete=models.CASCADE,
#     #                              null=True, blank=True)
#     # users = models.ManyToManyField(UserInformation,
#     #                                related_name='users_role',
#     #                                verbose_name='用户',
#     #                                help_text='用户角色，控制用户访问与数据修改权限', blank=True)
#     # ranges_dadui = models.ManyToManyField(DaDuiType, verbose_name='权限大队', help_text='可以访问的数据范围：大队', blank=True)
#     # ranges_zhongdui = models.ManyToManyField(ZhongDuiType, verbose_name='权限中队（小组）',
#     #                                          help_text='可以访问的数据范围：中队（小组），要选择此项必须选择大队选项',
#     #                                          blank=True)
#
#     # 创建时间
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     # 最后更新时间
#     update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
#     # 是否删除
#     is_delete = models.BooleanField(default=False, verbose_name='是否删除')
#
#     class Meta:
#         verbose_name = '角色'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


# # 角色模型
# class Role(models.Model):
#     name = models.CharField(max_length=25, verbose_name='角色名称', help_text='角色名称')
#     ranges_fenzu = models.ManyToManyField(DaduiZhongduiType, verbose_name='权限范围', help_text='角色控制数据的权限范围', blank=True)
#     group = models.OneToOneField(Group, verbose_name='用户组', help_text='与角色对应的用户组，控制角色权限', on_delete=models.CASCADE,
#                                  null=True, blank=True)
#     # users = models.ManyToManyField(UserInformation,
#     #                                related_name='users_role',
#     #                                verbose_name='用户',
#     #                                help_text='用户角色，控制用户访问与数据修改权限', blank=True)
#     # ranges_dadui = models.ManyToManyField(DaDuiType, verbose_name='权限大队', help_text='可以访问的数据范围：大队', blank=True)
#     # ranges_zhongdui = models.ManyToManyField(ZhongDuiType, verbose_name='权限中队（小组）',
#     #                                          help_text='可以访问的数据范围：中队（小组），要选择此项必须选择大队选项',
#     #                                          blank=True)
#
#     # 创建时间
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     # 最后更新时间
#     update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
#     # 是否删除
#     is_delete = models.BooleanField(default=False, verbose_name='是否删除')
#
#     class Meta:
#         verbose_name = '角色'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
'''


# 用户模型.
class UserInformation(AbstractUser):
    # avatar = models.ImageField(upload_to='avatar/%Y/%m',
    #                            default='avatar/default.png',
    #                            max_length=200, blank=True,
    #                            null=True,
    #                            verbose_name='用户头像')
    # qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    # wx = models.CharField(max_length=50, blank=True, null=True, verbose_name='微信号码')
    # role = models.ManyToManyField(Group, verbose_name='角色', help_text='角色权限', blank=True)
    fenzu = models.ManyToManyField(DaduiZhongduiType, verbose_name='权限范围', help_text='角色控制数据的权限范围', blank=True)

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name='角色',
    #     blank=True,
    #     help_text='角色权限',
    #     related_name="user_set",
    #     related_query_name="user",
    # )

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        if self.last_name:
            return '{}-{}{}'.format(self.username, self.last_name, self.first_name)
        else:
            return self.username


img_type = (('登记照', '登记照'), ('党团材料', '党团材料'))


# 档案图片
class ImgData(models.Model):
    user = models.ForeignKey(UserInformation, verbose_name='上传人', on_delete=models.SET_NULL, null=True, blank=True)
    img_data = models.ImageField(upload_to='avatar/personal/%Y/%m/%d',
                                 default='avatar/default.jpg',
                                 max_length=200, blank=True,
                                 null=True,
                                 verbose_name='档案图片')
    type = models.CharField(max_length=10, verbose_name='图片类型',
                            help_text='图片类型', default='',
                            choices=img_type)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '档案图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.user, self.type)


# 人员档案
class PersonalInformation(models.Model):
    user = models.OneToOneField(UserInformation, verbose_name='用户', on_delete=models.CASCADE,
                                help_text='关联的账号，一对一关联，必须唯一')
    personal_avatar = models.OneToOneField(ImgData, verbose_name='登记照', on_delete=models.SET_NULL, null=True, blank=True)
    idfj = models.CharField(max_length=10, verbose_name='辅警编号', help_text='辅警编号', default='未分配')
    name = models.CharField(max_length=10, verbose_name='姓名', help_text='姓名', db_index=True)
    named = models.CharField(max_length=10, verbose_name='曾用名', default='无', help_text='曾用名')
    nation = models.CharField(max_length=10, verbose_name='民族', default='汉族', choices=NATION, help_text='民族')
    sex = models.CharField(max_length=5, verbose_name='性别', choices=(('男', '男'), ('女', '女')), default='男',
                           help_text='性别，默认为“男”,系统会根据身份证自动判断')
    birthday = models.DateField(verbose_name='出生日期', help_text='出生日期，系统会根据身份证自动填写', blank=True)
    zodiac = models.CharField(verbose_name='生肖', max_length=5, default='不清',
                              choices=(('不清', '不清'), ('猴', '猴'), ('鸡', '鸡'), ('狗', '狗'), ('猪', '猪'), ('鼠', '鼠'),
                                       ('牛', '牛'), ('虎', '虎'), ('兔', '兔'), ('龙', '龙'), ('蛇', '蛇'), ('马', '马'),
                                       ('羊', '羊')), help_text='生肖，系统会根据身份证自动填写')
    constellation = models.CharField(verbose_name='星座', max_length=6, default='不清',
                                     choices=(('不清', '不清'), ('摩羯座', '摩羯座'), ('水瓶座', '水瓶座'), ('双鱼座', '双鱼座'),
                                              ('白羊座', '白羊座'), ('金牛座', '金牛座'), ('双子座', '双子座'), ('巨蟹座', '巨蟹座'),
                                              ('狮子座', '狮子座'), ('处女座', '处女座'), ('天秤座', '天秤座'), ('天蝎座', '天蝎座'),
                                              ('射手座', '射手座')), help_text='星座，系统会根据身份证自动填写')
    idnumber = models.CharField(max_length=18, verbose_name="身份证", help_text="身份证号，如果最后一位为X请大写，字段在数据库中必须唯一",
                                db_index=True, unique=True)
    jiguan = models.ForeignKey(DiZhi, verbose_name='籍贯', on_delete=models.SET_NULL, null=True, blank=True,
                               help_text='籍贯，系统会根据身份证自动填写')
    permanent = models.CharField(max_length=100, verbose_name='户籍地址', help_text='身份证上的地址')
    permanenttype = models.ForeignKey(PermanentType, verbose_name="户籍类别", help_text='户籍类别',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    home = models.CharField(max_length=100, verbose_name='现居地址', help_text='现在居住的地址，能联系到的，可以和户籍地址相同')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号码', help_text='手机号码，字段在数据库中必须唯一"')
    hobby = models.CharField(max_length=100, verbose_name='爱好/特长', default='无', help_text='爱好/特长')
    """↓单独创建一个党团关系表↓"""
    # politics = models.CharField(max_length=10,
    #                             choices=(("群众", "群众"), ("共青团员", "共青团员"), ("中共党员", "中共党员"),),
    #                             verbose_name='政治面貌', help_text='政治面貌',
    #                             default="群众")
    # politicstime = models.DateField(verbose_name='入党/团时间', null=True, blank=True, help_text='入党/团时间')
    """↑单独创建一个党团关系表↑"""
    veteran = models.ForeignKey(DemobilizedType, verbose_name='退役类别', on_delete=models.SET_NULL, null=True,
                                blank=True, help_text='退役类别')
    marriage = models.ForeignKey(Marriage, max_length=10, verbose_name='婚姻状态', help_text='婚姻状态',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    drivinglicense = models.ForeignKey(DrivingLicenseType, verbose_name='驾照', on_delete=models.SET_NULL, null=True,
                                       blank=True, default=1, help_text='驾照')
    """以下可以设计为在职履历信息（单独设计一个关联的ForeignKey表）"""
    # entry = models.DateField(verbose_name='入职时间', null=True, blank=True, help_text='入职时间，本信息由管理员填写')
    # entryzhuanzheng = models.DateField(verbose_name='入职转正时间', null=True, blank=True,
    #                                    help_text='入职转正时间，本信息由管理员填写（辅警不填写此项）')
    # zhuanfujing = models.DateField(verbose_name='辅警入职时间', null=True, blank=True, help_text='辅警入职时间，本信息由管理员填写')
    # fujingzhuanzheng = models.DateField(verbose_name='辅警入职转正时间', null=True, blank=True,
    #                                     help_text='辅警入职转正时间，本信息由管理员填写（协勤不填写此项）')
    """以上可以设计为在职履历信息（单独设计一个关联的ForeignKey表）"""
    """↓已加入用工信息表↓"""
    # category = models.ForeignKey(CategoryType, verbose_name='人员类别', on_delete=models.SET_NULL, null=True, blank=True,
    #                              help_text='人员类别，本信息由管理员填写')
    # gangweitype = models.ForeignKey(PostType, verbose_name='岗位类别', on_delete=models.SET_NULL, null=True, blank=True,
    #                                 help_text='岗位类别，本信息由管理员填写')
    # gangweiname = models.ForeignKey(PostName, verbose_name='岗位名称', on_delete=models.SET_NULL, null=True, blank=True,
    #                                 help_text='岗位名称，本信息由管理员填写')
    # quit = models.DateField(verbose_name='离职/调离时间', null=True, blank=True, help_text='离职/调离时间，本信息由管理员填写')
    """↑已加入用工信息表↑"""
    """以下信息准备改写（已改写）"""
    # dadui = models.ForeignKey(DaDuiType, verbose_name='所属大队', on_delete=models.SET_NULL, null=True, blank=True,
    #                           help_text='所属大队，本信息由管理员填写')
    dadui = models.ForeignKey(DaduiZhongduiType, verbose_name='所属大队', on_delete=models.SET_NULL, null=True, blank=True,
                              help_text='所属大队，本信息由管理员填写', related_name="dadui_type")
    # zhongdui = models.ForeignKey(ZhongDuiType, verbose_name='所属中队（小组）', on_delete=models.SET_NULL, null=True,
    #                              blank=True, help_text='所属中队（小组），本信息由管理员填写')
    fenzu = models.ForeignKey(DaduiZhongduiType, verbose_name='所属分组', on_delete=models.SET_NULL, null=True,
                              blank=True, help_text='所属分组，本信息由管理员填写', related_name="fenzu_type")
    """以上信息准备改写"""
    jiediao = models.ForeignKey(Borrow, verbose_name='借调位置', on_delete=models.SET_NULL, null=True, blank=True,
                                help_text='借调位置，本信息由管理员填写')
    bianzhi = models.ForeignKey(Organization, verbose_name='编制位置', on_delete=models.SET_NULL, null=True, blank=True,
                                help_text='编制位置，本信息由管理员填写')
    economics = models.ForeignKey(Economics, verbose_name='家庭经济状态', on_delete=models.SET_NULL, null=True, blank=True,
                                  help_text='家庭经济状态')
    sources = models.ForeignKey(Sources, verbose_name='家庭经济状态，经济来源', on_delete=models.SET_NULL, null=True, blank=True,
                                help_text='家庭经济状态，经济来源')

    beizhu = models.CharField(default='', verbose_name='备注', max_length=500, help_text='备注', blank=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '个人档案'
        verbose_name_plural = verbose_name
        ordering = ['dadui', 'fenzu']

    def save(self, *args, **kwargs):
        if self.idnumber:
            self.idfj = self.idfj.upper()
            self.idnumber = self.idnumber.upper()
            getInformation = GetInformation(self.idnumber.upper())
            shengri = getInformation.get_birthday()
            jiguan = getInformation.get_6()
            dizhi = DiZhi.objects.filter(dizhi_id=jiguan)
            if dizhi:
                self.jiguan = dizhi[0]
            # if self.entry:
            #     self.entryzhuanzheng = self.entry - relativedelta(months=-1)
            # if self.zhuanfujing:
            #     self.fujingzhuanzheng = self.zhuanfujing - relativedelta(months=-2)
            self.sex = getInformation.get_sex()
            self.birthday = datetime.date(*map(int, shengri.split('-')))
            self.zodiac = getInformation.get_zodiac()
            self.constellation = getInformation.get_constellation()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.fenzu, self.idnumber)


# 党团关系
class DangTuan(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', help_text='姓名', on_delete=models.CASCADE,
                             related_name='dangtuans')
    start = models.DateField(verbose_name='加入时间', help_text='开始时间', null=True, blank=True)
    end = models.DateField(verbose_name='退出时间', help_text='结束时间', null=True, blank=True)
    politics = models.ForeignKey(Politics, verbose_name='政治面貌', help_text='政治面貌', on_delete=models.DO_NOTHING)
    # is_effective = models.BooleanField(default=True, verbose_name='是否有效', help_text='是否有效')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '党团关系'
        verbose_name_plural = verbose_name
        ordering = ['-start', '-create_time']

    def __str__(self):
        return "%s-%s" % (self.name, self.politics)


# 用工信息
class YongGong(models.Model):
    """注意添加到履历信息中，本信息用于判断人员是否离职与调离、判断人员是否已转辅警、判断人员是否为直接考入人员"""
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', help_text='姓名', on_delete=models.CASCADE,
                             related_name='yonggongs')
    start = models.DateField(verbose_name='开始时间', help_text='开始时间（以第一次合同号的签订日期为准）')
    hetong_time = models.DateField(verbose_name='合同签订时间', help_text='合同签订时间')
    shixiqi = models.IntegerField(verbose_name='实习期', help_text='实习期（单位：月，type:int）')
    zhuanzheng = models.DateField(verbose_name='转正时间', help_text='转正时间（以第一次合同号的签订日期为准）')
    end = models.DateField(verbose_name='结束时间', help_text='结束时间', null=True, blank=True)
    yonggongtype = models.ForeignKey(YongGongType, verbose_name='用工方式', help_text='用工方式',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    hetong = models.IntegerField(verbose_name='合同期限（单位：年）', help_text='合同期限（单位：年，type:int）')
    position = models.CharField(verbose_name='工作单位', help_text='工作单位', max_length=250, default='重庆市公安局北碚区分局特警支队')
    dispatch = models.CharField(verbose_name='派遣公司', help_text='派遣公司', max_length=250, default='重庆市北碚区保安服务有限公司',
                                null=True, blank=True)
    shenfenguilei = models.ForeignKey(CategoryType, verbose_name='人员类别', help_text='人员类别', related_name="renyuan_type",
                                      on_delete=models.SET_NULL, null=True, blank=True)
    gangweitype = models.ForeignKey(CategoryType, verbose_name='岗位类别', on_delete=models.SET_NULL, null=True, blank=True,
                                    help_text='岗位类别，本信息由管理员填写', related_name="gangwei_type")
    gangweiname = models.ForeignKey(CategoryType, verbose_name='岗位名称', on_delete=models.SET_NULL, null=True, blank=True,
                                    help_text='岗位名称，本信息由管理员填写', related_name="gangweiname_type")
    post = models.CharField(verbose_name='身份或职务', help_text='身份或职务', max_length=250, default='队员')
    zhuangtai = models.ForeignKey(ZhuangTai, verbose_name='人员状态', on_delete=models.SET_NULL, null=True, blank=True,
                                  help_text='人员状态')
    remarks = models.CharField(verbose_name='备注', help_text='备注', max_length=250, default='', null=True, blank=True)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '用工信息'
        verbose_name_plural = verbose_name
        ordering = ['-start']

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.shenfenguilei, self.position)

    def save(self, *args, **kwargs):
        # print(self.start, self.shixiqi)
        self.zhuanzheng = self.start - relativedelta(months=-self.shixiqi)
        # if Lvli.objects.all():
        #     if not Lvli.objects.filter(name=self.name, position=self.position,
        #                                start=self.start):
        #         """新建履历信息"""
        #         lvli = Lvli()
        #         lvli.name = self.name
        #         lvli.start = self.start
        #         lvli.end = self.end
        #         lvli.position = self.position
        #         lvli.shenfenguilei = self.shenfenguilei
        #         lvli.post = self.post
        #         lvli.remarks = self.remarks
        #         lvli.save()
        #     if Lvli.objects.filter(name=self.name,
        #                            position=self.position,
        #                            start=self.start).exclude(end=self.end):
        #         """修改信息的情况"""
        #         lvli = Lvli.objects.get(name=self.name,
        #                                 position=self.position,
        #                                 start=self.start,
        #                                 shenfenguilei=self.shenfenguilei)
        #         lvli.end = self.end
        #         lvli.save()
        super().save(*args, **kwargs)


# 履历信息
class Lvli(models.Model):
    """注意与用工信息同步"""
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', help_text='姓名', on_delete=models.CASCADE,
                             related_name='lvlis')
    start = models.DateField(verbose_name='开始时间', help_text='开始时间')
    end = models.DateField(verbose_name='结束时间', help_text='结束时间', null=True, blank=True)
    position = models.CharField(verbose_name='工作单位', help_text='工作单位', max_length=250, default='重庆市公安局北碚区分局特警支队')
    shenfenguilei = models.ForeignKey(ShenFenGuiLei, verbose_name='身份归类', on_delete=models.DO_NOTHING)
    post = models.CharField(verbose_name='身份或职务', help_text='身份或职务', max_length=250, default='队员')
    remarks = models.CharField(verbose_name='备注', help_text='备注', max_length=250, default='')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '履历信息'
        verbose_name_plural = verbose_name
        ordering = ['-start']

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.shenfenguilei, self.position)


# 学历信息
class Education(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', on_delete=models.CASCADE,
                             related_name='educations')
    school = models.CharField(verbose_name='学校名称', max_length=50)
    xueli = models.ForeignKey(EducationType, verbose_name='学历', on_delete=models.DO_NOTHING)
    academicdegree = models.ForeignKey(AcademicDegreeType, verbose_name='学位', on_delete=models.SET_NULL, null=True,
                                       blank=True)
    graduation = models.CharField(verbose_name='毕业证书编号', unique=True, default='不清', max_length=50)
    degree = models.CharField(verbose_name='学位证书编号', unique=True, default='不清', max_length=50)
    start = models.DateField(verbose_name='入学时间')
    end = models.DateField(verbose_name='毕业时间')
    school_time = models.FloatField(verbose_name='学制（单位：年）', help_text='正常从入学到毕业需要的时间，填写数字', default=3)
    major = models.CharField(verbose_name='专业', help_text='所学专业，没有请填无', default='无', max_length=20)
    xuelisuoming = models.ForeignKey(XueLiInformation, verbose_name='学历说明', on_delete=models.DO_NOTHING)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '学历信息'
        verbose_name_plural = verbose_name
        ordering = ['-end']

    def __str__(self):
        return "%s-%s" % (self.name, self.school)


# 车辆信息
class Car(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', on_delete=models.CASCADE, related_name='car')
    vehicle = models.CharField(verbose_name='车牌号', unique=True, max_length=10, default="无", db_index=True)
    vehiclecategory = models.ForeignKey(CarType, verbose_name='车辆类别', on_delete=models.DO_NOTHING)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '车辆信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.name, self.vehicle)


# 家庭成员信息
class HomeInformation(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='本人信息', on_delete=models.CASCADE)
    names = models.CharField(max_length=10, verbose_name='姓名', db_index=True)
    nation = models.CharField(max_length=10, verbose_name='民族', default='汉族', choices=NATION)
    appellation = models.ForeignKey(ChengWei, verbose_name='称谓', on_delete=models.DO_NOTHING)
    xueli = models.ForeignKey(EducationType, verbose_name='学历', on_delete=models.DO_NOTHING)
    idnumber = models.CharField(max_length=18, verbose_name="身份证", help_text="如果最后一位为X请大写", unique=True, db_index=True)
    birthday = models.DateField(verbose_name='出生日期', null=True, blank=True, help_text='系统自动生成')
    politics = models.ForeignKey(Politics, verbose_name='政治面貌', on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号码')
    shenfenguilei = models.ForeignKey(ShenFenGuiLei, verbose_name='身份归类', on_delete=models.DO_NOTHING)
    renyuanxianzhuang = models.ForeignKey(RenYuanXianZhuang, verbose_name='人员现状', on_delete=models.DO_NOTHING)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '家庭成员信息'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.birthday and self.idnumber:
            shengri = GetInformation(self.idnumber).get_birthday()
            shengri = datetime.date(*map(int, shengri.split('-')))
            self.birthday = shengri
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s-%s" % (self.name, self.appellation)


# 个人体检信息
class PhysicalExamination(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', on_delete=models.CASCADE, related_name='tj')
    year = models.ForeignKey(Year, verbose_name='体检年份', on_delete=models.DO_NOTHING)
    result = models.ForeignKey(TiJianJieGuo, verbose_name='结果', on_delete=models.DO_NOTHING)
    information = models.TextField(verbose_name='体检结论')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '个人体检信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.name, self.year)


# 个人量体信息
class MeasureInformation(models.Model):
    name = models.ForeignKey(PersonalInformation, verbose_name='姓名', on_delete=models.CASCADE, related_name='lt')
    year = models.ForeignKey(Year, verbose_name='测量年份', on_delete=models.DO_NOTHING)
    shengao = models.FloatField(verbose_name='身高（CM）')
    tizhong = models.FloatField(verbose_name='体重（KG）')
    xiongwei = models.FloatField(verbose_name='胸围（CM）')
    jiankuan = models.FloatField(verbose_name='肩宽（CM）')
    xiuchang = models.FloatField(verbose_name='袖长（CM）')
    yaowei = models.FloatField(verbose_name='腰围（CM）')
    tunwei = models.FloatField(verbose_name='臀围（CM）')
    duwei = models.FloatField(verbose_name='肚围（CM）')
    kuchang = models.FloatField(verbose_name='裤长（CM）')
    datuiwei = models.FloatField(verbose_name='大腿围（CM）')
    maowei = models.FloatField(verbose_name='帽围（CM）')
    xiezi = models.FloatField(verbose_name='鞋子（码）')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '个人量体信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.name, self.year)
