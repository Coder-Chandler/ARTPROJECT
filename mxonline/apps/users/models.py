# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=50, default=u"", verbose_name=u"昵称")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), default="female", max_length=6)
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(verbose_name=u"用户头像", upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    def unread_nums(self):
        # 獲取用戶未讀消息數量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class Comment(models.Model):
    content = models.CharField(max_length=200)

    post_time = models.DateTimeField(auto_now_add=True)

    def _unicode_(self):
        return self.content


class Artists(models.Model):
    Artist_name = models.CharField(max_length=50, default=u"", verbose_name=u"作品名称")

    Artist_size = models.IntegerField(default=100, verbose_name=u"尺寸")

    Artist_image = models.ImageField(upload_to="image/%Y/%m", max_length=100)

    Artist_time = models.DateField(verbose_name=u"创作日期", default="")

    Artist_material = models.CharField(max_length=100, default=u"", verbose_name=u"作品材质")

    post_time = models.DateTimeField(auto_now_add=True)

    def _unicode_(self):
        return self.Artist_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码"), ('update_email', u'修改邮箱')), max_length=30)
    send_time = models.DateField(verbose_name=u"发送时间", default=datetime.now)

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=100, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


