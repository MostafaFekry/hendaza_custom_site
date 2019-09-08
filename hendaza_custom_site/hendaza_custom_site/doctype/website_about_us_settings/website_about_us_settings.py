# -*- coding: utf-8 -*-
# Copyright (c) 2019, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class WebsiteAboutUsSettings(Document):
	def on_update(self):
		from frappe.website.render import clear_cache
		clear_cache("aboutus")


def get_args():
	obj = frappe.get_doc("Website About Us Settings")
	return {
		"obj": obj
	}