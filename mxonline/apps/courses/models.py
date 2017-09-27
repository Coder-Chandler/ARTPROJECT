# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from organization.models import CourseOrg, Teacher
from DjangoUeditor.models import UEditorField
# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, default="", verbose_name=u'艺术家')
    name = models.CharField(max_length=50, verbose_name=u"作品名称")
    desc = models.CharField(max_length=300, verbose_name=u"作品描述")
    detail = UEditorField(verbose_name=u"作品详情", width=600, height=300,
                          imagePath="courses/ueditor/", filePath="courses/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
    teacher = models.ForeignKey(Teacher, verbose_name=u'讲师', null=True, blank=True)
    degree = models.CharField(verbose_name=u"类别", choices=(("sc", u"水彩"), ("yh", u"油画"), ("sm", u"素描"), ("bx", u"丙烯"),
                                                            ("tbh", u"炭笔画"), ("smh", u"水墨画"), ("fch", u"粉彩画"),
                                                            ("swys", u"数位艺术"), ("banh", u"版画"), ("boh", u"帛画"), ("bih", u"壁画"),), max_length=20)
    learn_times = models.IntegerField(default=0, verbose_name=u"作品用时(天)")
    students = models.IntegerField(default=0, verbose_name=u"点赞人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"关注人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default='艺术', max_length=20, verbose_name=u"作品列表")
    tag = models.CharField(default='', verbose_name=u'课程标签', max_length=10)
    need_know = models.CharField(default='', max_length=300, verbose_name=u"课程须知")
    teacher_tell = models.CharField(default='', max_length=300, verbose_name=u"老师告诉你")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"作品"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = '章节数'

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='https://zhuanlan.zhihu.com/c_117215506'>跳转</a>")
    go_to.short_description = '跳转'

    def get_learn_users(self):
        # 获取课程学习人数
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播作品'
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"作品")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    url = models.CharField(max_length=200, default='', verbose_name=u'访问地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

