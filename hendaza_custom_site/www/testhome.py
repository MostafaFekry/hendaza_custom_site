# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, fmt_money, flt, nowdate, getdate

no_cache = 1
no_sitemap = 1

def get_context(context):

	homepage = frappe.get_doc('Website Homepage')
	context.title = homepage.title or homepage.company
	if homepage.main_section == None:
		context.main_section = ''

	
	if homepage.slideshow:
		context.slideshow = homepage.slideshow
		context.update(get_slideshow_details(homepage.slideshow))

	if homepage.homepage_items_group:
		for items_group in homepage.homepage_items_group:
			item_group_name = frappe.get_doc("Item Group", items_group.item_group_name)
			if item_group_name:
				items_group.route = '/' + item_group_name.route
				items_group.image = item_group_name.image
				items_group.territory = item_group_name.territory
				items_group.unit_usage = item_group_name.unit_usage	
	
	if homepage.homepage_products_items:
		for products_items in homepage.homepage_products_items:
			product = frappe.get_doc("Item", products_items.item_code)
			if product:
				products_items.item_name = product.item_name
				products_items.route = '/' + product.route
				products_items.image = product.image
				products_items.territory = product.territory
				products_items.unit_usage = product.unit_usage
	
	context.homepage = homepage
	return context

def get_slideshow_details(slideshow):

	slideshow = frappe.get_doc("Website Slideshow", slideshow)
	if not slideshow:
		return {}

	return {
		"slides": slideshow.get({"doctype":"Website Slideshow Item"}),
		"slideshow_header": slideshow.header or ""
	}

