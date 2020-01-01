from django.db import models

# Create your models here.

from apps.users.models import PersonalInformation


class BaoBei(models.Model):
    """
    报备考勤表
    报备范围：出国、出市、出主城
    """
    name = models.ForeignKey(PersonalInformation, verbose_name='报备人', on_delete=models.CASCADE)
    shiyou = models.CharField(max_length=10, verbose_name='报备事由', default='出主城',
                              choices=(('出主城', '出主城'), ('出重庆', '出重庆'), ('出国', '出国')))
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')


class QingJia(models.Model):
    """
    请假考勤表
    考勤范围：事假、病假、丧假、婚假、年休假、2小时假
    """
    name = models.ForeignKey(PersonalInformation, verbose_name='请假人', on_delete=models.CASCADE)
    jiabie = models.CharField(verbose_name='假别', max_length=10, default='事假',
                              choices=(("事假", "事假"), ("病假", "病假"), ("婚假", "婚假"), ("年休假", "年休假"),
                                       ("产假", "产假"), ("陪产假", "陪产假"), ("丧假", "丧假"), ("2小时", "2小时"),), )
    shiyou = models.TextField(verbose_name='请假事由', default='', help_text='详细请假原因')
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')
    day = models.FloatField(verbose_name='请假天数', help_text='由系统自动生成')
    beizhu = models.CharField(verbose_name='备注', max_length=100)
    # img = models.ManyToManyField(verbose_name='图片材料')
    baobei = models.ForeignKey(BaoBei, verbose_name='是否外出报备', help_text='如果有出主城、出重庆、出国请则选择这一项',
                               on_delete=models.SET_NULL, null=True, blank=True)


class BuJiaShenQing(models.Model):
    """补假申请表"""
    name = models.ManyToManyField(PersonalInformation, verbose_name='补假人（可以为多个）',
                                  related_name='bj', related_query_name='pi')
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')
    day = models.FloatField(verbose_name='补假天数', help_text='由系统自动生成')
    baobei = models.ForeignKey(BaoBei, verbose_name='是否外出报备', help_text='如果有出主城、出重庆、出国请则选择这一项',
                               on_delete=models.SET_NULL, null=True, blank=True)


class JiaBan(models.Model):
    """加班申请表"""
    name = models.ManyToManyField(PersonalInformation, verbose_name='加班人(可以为多个)')
    shiyou = models.TextField(verbose_name='加班事由', default='', help_text='加班的原因')
    jiabanleixing = models.CharField(verbose_name='加班类型', max_length=10, default='',
                                     choices=(('工作日加班', '工作日加班'), ('双休日加班', '双休日加班'), ('节假日加班', '节假日加班')))
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')
    timedata = models.FloatField(verbose_name='共计加班时间', help_text='由系统自动生成')
    buchang = models.CharField(verbose_name='加班补偿', max_length=10, default='',
                               choices=(('发放加班费', '发放加班费'), ('安排补假', '安排补假')))


class HuanBan(models.Model):
    """换班考勤表"""
    named = models.ForeignKey(PersonalInformation, verbose_name='换班人', on_delete=models.CASCADE)
    name = models.ForeignKey(PersonalInformation, verbose_name='代班人', on_delete=models.CASCADE)
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')
    timedata = models.FloatField(verbose_name='共计代班时间', help_text='由系统自动生成')


class KaoHe(models.Model):
    """考核详情表(请假考核手动添加，后期改为系统自动关联请假考核，并添加删除标记，标记是否月底考核)"""
    name = models.ManyToManyField(PersonalInformation, verbose_name='被考核人(可以为多个)')
    kaoheshijian = models.DateField(verbose_name='被考核时间')
    kaoheleixing = models.CharField(verbose_name='考核类型', max_length=4, default='',
                                    choices=(('公共项目', '公共项目'), ('绩效项目', '绩效项目'), ('组织测评', '组织测评')))
    fenzhi = models.SmallIntegerField(verbose_name='分值', help_text='加分或者减分，可以为负数')
    yuanyin = models.CharField(verbose_name='原因', help_text='加/减分原因', max_length=250, default='')
    yiju = models.CharField(verbose_name='加/减分依据', help_text='考核管理办法中的条款', max_length=300)
    beizhu = models.CharField(verbose_name='备注', max_length=150)
