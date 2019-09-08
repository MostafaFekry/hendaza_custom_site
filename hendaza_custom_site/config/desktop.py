# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Hendaza Custom Site",
			"category": "Places",
			"label": _("Hendaza Custom Site"),
			"color": "#bdc3c7",
			"reverse": 1,
			"icon": "octicon octicon-globe",
			"type": "module",
			"description": "Custom site for Hendaza."
		}
	]
