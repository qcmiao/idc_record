# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from idc.models import *
# Register your models here.

admin.site.site_header = 'IDC备案管理'
admin.site.site_title = 'IDC备案管理'
# admin.site.empty_value_display = '暂无'


@admin.register(IpInfo)
class IdcAdmin(admin.ModelAdmin):
	empty_value_display = '暂无'

	list_display = ('ip', 'show_domaininfo', 'custom_info', 'sales_men')

	def show_domaininfo(self, obj):
		return [i.domain_name for i in obj.domain_info.all()]
	show_domaininfo.short_description = '域名名称'
	filter_horizontal = ('domain_info',)
	list_display_links = ('ip',)
	list_per_page = 20

	ordering = ('-id',)
	list_filter = ('app_purpose',)
	search_fields = ('ipaddr',)
	fk_fields = ('app_purpose',)



@admin.register(DomainInfo)
class DomainAdmin(admin.ModelAdmin):
	list_display = ('domain_name', 'website', 'domain_ip', 'MIIT_number', 'MPS_number')
	fieldsets = (
		('域名信息', {'fields': ['website', ('domain_name', 'domain_ip'), ('MIIT_number', 'MPS_number')]}),
	)


@admin.register(CustomInfo)
class CustomAdmin(admin.ModelAdmin):
	list_display = ('name', 'businessmen_name', 'technicians_name', 'emergency_name')
	fieldsets = (
		('客户公司信息', {'fields': [('name', 'address'), ('va_licence', 'business_licence'),]}),
		('业务联系人信息', {'fields': [('businessmen_name','businessmen_telephone', 'businessmen_mobile', 'businessmen_id_type', 'businessmen_id_number')]}),
		('技术人员信息', {'fields': [('technicians_name', 'technicians_mobile', 'technicians_email')]}),
		('紧急联系人信息', {'fields': [('emergency_name','emergency_mobile')]})
	)


@admin.register(Salesmen)
class SalesmenAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fieldsets = (
		('销售信息', {'fields': ['name']}),
	)
# admin.site.register([Ipinfo])
