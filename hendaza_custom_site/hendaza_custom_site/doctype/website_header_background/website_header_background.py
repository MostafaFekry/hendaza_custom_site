# -*- coding: utf-8 -*-
# Copyright (c) 2019, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class WebsiteHeaderBackground(Document):
	pass

def get_website_header_background_details(page_header_background):
	if not page_header_background:
		return {}
		
	page_header_background = frappe.get_doc("Website Header Background", page_header_background)
	return {
		"header_background_image": page_header_background.header_background_image or ""
	}