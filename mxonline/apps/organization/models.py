# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"艺术家名称")
    desc = models.TextField(verbose_name=u"艺术家描述")
    home_img = models.ImageField(default='1200*800大图',upload_to="org/%Y/%m", verbose_name=u"主页大图", max_length=100)
    tag = models.CharField(default='画者', max_length=4, verbose_name=u"艺术家标签")
    category = models.CharField(default='hh', verbose_name=u"艺术家类别", max_length=20, choices=(('hh', '绘画'), ('dk', '雕塑'), ('ty', '陶艺')))
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"关注数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图", max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"艺术家地址")
    city = models.ForeignKey(CityDict, default='', verbose_name=u"所在城市")
    students = models.IntegerField(default=0, verbose_name=u'点赞人数')
    courses_nums = models.IntegerField(default=0, verbose_name=u'作品数')
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"艺术家"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取课程机构的教师的数量
        return self.teacher_set.all().count()

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"教师名")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(default='', upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()

