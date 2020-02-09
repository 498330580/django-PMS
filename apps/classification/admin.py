from django.contrib import admin

# Register your models here.

from classification.models import *


class Classification(admin.ModelAdmin):
    list_display = ('name',)


class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)


admin.site.register(CategoryType, Classification)
admin.site.register(DaduiZhongduiType)
admin.site.register(DemobilizedType, Classification)
admin.site.register(DrivingLicenseType, Classification)
# admin.site.register(DaDuiType, Classification)
# admin.site.register(ZhongDuiType, Classification)
admin.site.register(Organization, Classification)
admin.site.register(Borrow, Classification)
admin.site.register(Economics, Classification)
admin.site.register(Sources, Classification)
# admin.site.register(ParentalInformation, Classification)
admin.site.register(EducationType, Classification)
admin.site.register(AcademicDegreeType, Classification)
admin.site.register(CarType, Classification)
# admin.site.register(PostType, Classification)
# admin.site.register(PostName, Classification)
admin.site.register(XueLiInformation, Classification)
admin.site.register(RenYuanXianZhuang, Classification)
admin.site.register(ShenFenGuiLei, Classification)
admin.site.register(ChengWei, Classification)
admin.site.register(TiJianJieGuo, Classification)
admin.site.register(Year, YearAdmin)
