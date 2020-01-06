from django.db import models


# Create your models here.

class Menu(models.Model):
    """
    菜单设置
    """
    CATEGORY_TYPE = (
        (1, "一级菜单"),
        (2, "二级菜单"),
        (3, "三级菜单"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="菜单名称", help_text="菜单名称")
    desc = models.TextField(default="", verbose_name="菜单描述", help_text="菜单描述")
    index = models.IntegerField(default=999, verbose_name='菜单顺序')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类菜单级别", help_text="父菜单",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    class_img = models.CharField(default="", max_length=100, verbose_name="class图标", help_text="Element图标")
    is_look = models.BooleanField(default=False, verbose_name="是否显示", help_text="是否显示到菜单中")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = "菜单设置"
        verbose_name_plural = verbose_name
        ordering = ['index']

    def __str__(self):
        return "%s-%s" % (self.category_type, self.name)
