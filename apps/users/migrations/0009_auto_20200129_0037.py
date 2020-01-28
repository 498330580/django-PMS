# Generated by Django 3.0.2 on 2020-01-29 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0002_auto_20200119_2145'),
        ('users', '0008_auto_20200129_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='beizhu',
            field=models.CharField(default='', help_text='备注', max_length=500, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='bianzhi',
            field=models.ForeignKey(blank=True, help_text='编制位置，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.Organization', verbose_name='编制位置'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='birthday',
            field=models.DateField(blank=True, help_text='出生日期，系统会根据身份证自动填写', verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='category',
            field=models.ForeignKey(blank=True, help_text='人员类别，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.CategoryType', verbose_name='人员类别'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='constellation',
            field=models.CharField(choices=[('不清', '不清'), ('摩羯座', '摩羯座'), ('水瓶座', '水瓶座'), ('双鱼座', '双鱼座'), ('白羊座', '白羊座'), ('金牛座', '金牛座'), ('双子座', '双子座'), ('巨蟹座', '巨蟹座'), ('狮子座', '狮子座'), ('处女座', '处女座'), ('天秤座', '天秤座'), ('天蝎座', '天蝎座'), ('射手座', '射手座')], default='不清', help_text='星座，系统会根据身份证自动填写', max_length=6, verbose_name='星座'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='dadui',
            field=models.ForeignKey(blank=True, help_text='所属大队，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.DaDuiType', verbose_name='所属大队'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='entry',
            field=models.DateField(blank=True, help_text='入职时间，本信息由管理员填写', null=True, verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='entryzhuanzheng',
            field=models.DateField(blank=True, help_text='入职转正时间，本信息由管理员填写（辅警不填写此项）', null=True, verbose_name='入职转正时间'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='fujingzhuanzheng',
            field=models.DateField(blank=True, help_text='辅警入职转正时间，本信息由管理员填写（协勤不填写此项）', null=True, verbose_name='辅警入职转正时间'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gangweiname',
            field=models.ForeignKey(blank=True, help_text='岗位名称，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.PostName', verbose_name='岗位名称'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='gangweitype',
            field=models.ForeignKey(blank=True, help_text='岗位类别，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.PostType', verbose_name='岗位类别'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='jiediao',
            field=models.ForeignKey(blank=True, help_text='借调位置，本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.Borrow', verbose_name='借调位置'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='jiguan',
            field=models.ForeignKey(blank=True, help_text='籍贯，系统会根据身份证自动填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.DiZhi', verbose_name='籍贯'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='quit',
            field=models.DateField(blank=True, help_text='离职/调离时间，本信息由管理员填写', null=True, verbose_name='离职/调离时间'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='sources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.Sources', verbose_name='家庭经济状态，经济来源'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='zhongdui',
            field=models.ForeignKey(blank=True, help_text='所属中队（小组），本信息由管理员填写', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classification.ZhongDuiType', verbose_name='所属中队（小组）'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='zhuanfujing',
            field=models.DateField(blank=True, help_text='辅警入职时间，本信息由管理员填写', null=True, verbose_name='辅警入职时间'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='zhuangtai',
            field=models.CharField(choices=[('在岗', '在岗'), ('离职', '离职'), ('调离', '调离')], default='在岗', help_text='人员状态', max_length=6, verbose_name='人员状态'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='zodiac',
            field=models.CharField(choices=[('不清', '不清'), ('猴', '猴'), ('鸡', '鸡'), ('狗', '狗'), ('猪', '猪'), ('鼠', '鼠'), ('牛', '牛'), ('虎', '虎'), ('兔', '兔'), ('龙', '龙'), ('蛇', '蛇'), ('马', '马'), ('羊', '羊')], default='不清', help_text='生肖，系统会根据身份证自动填写', max_length=5, verbose_name='生肖'),
        ),
    ]