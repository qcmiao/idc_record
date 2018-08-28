# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Salesmen(models.Model):
	name = models.CharField('销售姓名', max_length=40, null=True)

	class Meta:
		verbose_name = '销售信息'
		verbose_name_plural = '销售信息'

	def __unicode__(self):
		return "{}".format(self.name)


class DomainInfo(models.Model):
	website = models.CharField('网站名称', max_length=40, blank=True, null=True)
	domain_name = models.CharField('域名名称', max_length=40, blank=True, null=True)
	domain_ip = models.CharField('域名对应IP', max_length=200, blank=True, null=True)
	MIIT_number = models.CharField('工信部备案号', max_length=40, blank=True, null=True)
	MPS_number = models.CharField('公安局备案号', max_length=40, blank=True, null=True)

	class Meta:
		verbose_name = '域名信息'
		verbose_name_plural = '域名信息'

	def __unicode__(self):
		return "{}  {}".format(self.domain_name, self.website)






ID_TYPE_CHOICES = (
	('IdCard', u'身份证'),
	('DriveCard', u'驾驶证'),
)


class CustomInfo(models.Model):
	name = models.CharField('客户名称', max_length=40, blank=True, null=True)
	va_licence = models.CharField('增值业务经营许可证号', max_length=40, blank=True, null=True)
	business_licence = models.CharField('单位营业执照', max_length=40, blank=True, null=True)
	address = models.CharField('单位地址', max_length=40, blank=True, null=True)
	businessmen_name = models.CharField('业务联系人姓名', max_length=40, blank=True, null=True)
	businessmen_id_type = models.CharField('业务联系人证件类型', max_length=40, choices=ID_TYPE_CHOICES, default='IdCard')
	businessmen_id_number = models.CharField('业务联系人证件号码', max_length=40, blank=True, null=True)
	businessmen_telephone = models.CharField('业务联系人固定电话', max_length=40, blank=True, null=True)
	businessmen_mobile = models.CharField('业务联系人移动电话', max_length=40, blank=True, null=True)
	technicians_name = models.CharField('技术联系人姓名', max_length=40, blank=True, null=True)
	technicians_mobile = models.CharField('技术联系人移动电话', max_length=40, blank=True, null=True)
	technicians_email = models.EmailField('技术联系人邮箱', blank=True, null=True)
	emergency_name = models.CharField('紧急联系人姓名', max_length=40, blank=True, null=True)
	emergency_mobile = models.CharField('紧急联系人移动电话', max_length=40, blank=True, null=True)

	class Meta:
		verbose_name = '客户信息'
		verbose_name_plural = '客户信息'

	def __unicode__(self):
		return "{}".format(self.name)


INTERNET_PROMISE_CHOICES = (
	('1', u'有'),
	('0', u'无'),
)


class IpInfo(models.Model):
	ipaddr = models.TextField(
		'IP地址',
		max_length=200
	)
	app_purpose = models.CharField('应用用途',
		max_length=40,
		blank=True,
		null=True
	)
	domain_info = models.ManyToManyField(
		DomainInfo,
		blank=True,
		null=True
	)
	custom_info = models.ForeignKey(
		CustomInfo,
		verbose_name='客户信息',
		blank=True, null=True,
		on_delete=models.SET_NULL
	)
	sales_men = models.ForeignKey(
		Salesmen,
		verbose_name='销售信息',
		blank=True,
		null=True,
		on_delete=models.SET_NULL
	)
	internetpromise = models.CharField(
		'互联网承诺书',
		max_length=10,
		choices=INTERNET_PROMISE_CHOICES,
		default='1',
		null=True
	)

	class Meta:
		verbose_name = 'IDC备案信息'
		verbose_name_plural = 'IDC备案信息'

	def ipaddress(self):
		if len(self.ipaddr) > 20:
			return '{0} ...'.format(self.ipaddr[0:19])
		else:
			return self.ipaddr
	ipaddress.short_description = 'IP地址'
	ip = property(ipaddress)
	# ipaddress.allow_tags = True

	def __unicode__(self):
		return "{}".format(self.ipaddr)
