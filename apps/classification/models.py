from django.db import models

# Create your models here.


# 人员类别
class CategoryType(models.Model):
    name = models.CharField(verbose_name='人员类别名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '人员类别信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 退伍军人类别
class DemobilizedType(models.Model):
    name = models.CharField(verbose_name='退伍军人名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '退伍军人信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 驾照类别
class DrivingLicenseType(models.Model):
    name = models.CharField(verbose_name='驾照类别名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '驾照类别信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# # 大队类别
# class DaDuiType(models.Model):
#     name = models.CharField(verbose_name='大队类别名称', max_length=10, db_index=True)
#     introduce = models.TextField(verbose_name='类别介绍')
#     index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')
#
#     # 创建时间
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     # 最后更新时间
#     update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
#     # 是否删除
#     is_delete = models.BooleanField(default=False, verbose_name='是否删除')
#
#     class Meta:
#         verbose_name = '大队类别信息'
#         verbose_name_plural = verbose_name
#         ordering = ['index', 'id']
#
#     def __str__(self):
#         return self.name
#
#
# # 中队（小组）类别
# class ZhongDuiType(models.Model):
#     name = models.CharField(verbose_name='中队（小组）类别名称', max_length=10, db_index=True)
#     introduce = models.TextField(verbose_name='类别介绍')
#     index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')
#
#     # 创建时间
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     # 最后更新时间
#     update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
#     # 是否删除
#     is_delete = models.BooleanField(default=False, verbose_name='是否删除')
#
#     class Meta:
#         verbose_name = '中队（小组）类别信息'
#         verbose_name_plural = verbose_name
#         ordering = ['index', 'id']
#
#     def __str__(self):
#         return self.name


class DaduiZhongduiType(models.Model):
    """
    大队、中队、小组设置
    """
    CATEGORY_TYPE = (
        ("人员", "人员"),
        ("大队", "大队"),
        ("中队", "中队"),
        ("小组", "小组"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="分组名称", help_text="分组名称")
    desc = models.TextField(default="", verbose_name="分组描述", help_text="分组描述")
    index = models.IntegerField(default=999, verbose_name='菜单顺序')
    category_type = models.CharField(choices=CATEGORY_TYPE, max_length=10, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类级别", help_text="父分组",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = "大队、中队、小组设置"
        verbose_name_plural = verbose_name
        ordering = ['index']

    def __str__(self):
        if self.parent_category:
            return '%s-%s' % (self.parent_category, self.name)
        else:
            return self.name


# 编制位置
class Organization(models.Model):
    name = models.CharField(verbose_name='编制名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='编制介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '编制信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 借调位置
class Borrow(models.Model):
    name = models.CharField(verbose_name='位置名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='位置介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '借调位置信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 经济状态
class Economics(models.Model):
    """良好、较好、一般、贫困等"""
    name = models.CharField(verbose_name='经济状态名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='经济状态介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '经济状态分类信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 经济来源
class Sources(models.Model):
    """经商、务工、务农等"""
    name = models.CharField(verbose_name='来源名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='来源介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '经济来源分类信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# # 父母状态，是否单亲等
# class ParentalInformation(models.Model):
#     """是否单亲家庭"""
#     name = models.CharField(verbose_name='父母状态名称', max_length=10)
#     introduce = models.TextField(verbose_name='状态介绍')
#
#     class Meta:
#         verbose_name = '父母状态分类信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


# 学历类型
class EducationType(models.Model):
    name = models.CharField(verbose_name='学历名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '学历类型信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 学位类型
class AcademicDegreeType(models.Model):
    name = models.CharField(verbose_name='学位名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '学位类型信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 车辆类别
class CarType(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '车辆类别信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 岗位类别
class PostType(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=10)
    introduce = models.TextField(verbose_name='类别介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '岗位类别信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 岗位名称
class PostName(models.Model):
    name = models.CharField(verbose_name='岗位名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='岗位介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '岗位名称信息'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 学历说明
class XueLiInformation(models.Model):
    name = models.CharField(verbose_name='学历说明名称', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='学历说明介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '学历说明分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 人员现状
class RenYuanXianZhuang(models.Model):
    name = models.CharField(verbose_name='人员现状', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='说明介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '人员现状'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 身份归类（亲属信息）
class ShenFenGuiLei(models.Model):
    name = models.CharField(verbose_name='身份归类', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='说明介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '身份归类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 称谓
class ChengWei(models.Model):
    name = models.CharField(verbose_name='称谓', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='说明介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '称谓'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 体检结果
class TiJianJieGuo(models.Model):
    name = models.CharField(verbose_name='体检结果', max_length=10, db_index=True)
    introduce = models.TextField(verbose_name='说明介绍')
    index = models.IntegerField(default=999, verbose_name='分类排序(从小到大)')

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '体检结果'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


# 体检年份
class Year(models.Model):
    year = models.IntegerField(verbose_name='体检年份', default=2019, unique=True, db_index=True)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '体检年份'
        verbose_name_plural = verbose_name
        ordering = ['year']

    def __str__(self):
        return '%s' % self.year


# 籍贯编码
class DiZhi(models.Model):
    dizhi_id = models.CharField(verbose_name='籍贯编码', default='无', max_length=6, unique=True, db_index=True)
    jiguan = models.CharField(verbose_name='籍贯', default='无', max_length=50)

    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '籍贯编码'
        verbose_name_plural = verbose_name

    def __str__(self):
        # return '%s-%s' % (self.dizhi_id, self.jiguan)
        return self.jiguan
