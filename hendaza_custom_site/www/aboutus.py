# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
from hendaza_custom_site.hendaza_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

no_cache = 1
no_sitemap = 1

def get_context(context):
	context.doc = frappe.get_doc("Website About Us Settings", "About Us Settings")
	
	context.title = context.doc.title or "About us"
	context.light_description = context.doc.light_description or ""
	
	if context.doc.page_header_background:
		context.update(get_website_header_background_details(context.doc.page_header_background))
	
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]

	return context
