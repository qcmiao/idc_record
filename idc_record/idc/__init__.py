# -*- coding: utf-8 -*-

from django.apps import AppConfig
import os

default_app_config = 'idc.IdcConfig'


def get_current_app_name(_file):
	return os.path.split(os.path.dirname(_file))[-1]


class IdcConfig(AppConfig):
	name = get_current_app_name(__file__)
	verbose_name = u"1-IDC备份管理系统"
