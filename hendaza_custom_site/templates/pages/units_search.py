# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, nowdate, cint
from erpnext.setup.doctype.item_group.item_group import get_item_for_list_in_html
from erpnext.shopping_cart.product_info import set_product_info_for_website

no_cache = 1
no_sitemap = 1

def get_context(context):
	context.show_search = True
	context.page_length = cint(frappe.db.get_single_value('Products Settings', 'products_per_page')) or 6
	context.title = "Units Search"
	
	territory_name = frappe.db.sql("""\
	select T.territory_name, T.name from `tabTerritory` T inner join `tabItem` I on T.name = I.territory where I.disabled =0 and I.show_in_website = 1 group by T.territory_name order by T.territory_name asc""", as_dict=1)
	context["search_territory_item"] = [d for d in territory_name]
	
	unit_usage = frappe.db.sql("""\
	select UU.unit_usage, UU.name from `tabUnit Usage` UU inner join `tabItem` I on UU.name = I.unit_usage where I.disabled =0 and I.show_in_website = 1 group by UU.unit_usage order by UU.unit_usage asc""", as_dict=1)
	context["search_unit_usage_item"] = [d for d in unit_usage]
	
	unit_for = frappe.db.sql("""\
	select AV.attribute_value, AV.name from `tabItem Attribute Value` AV inner join `tabItem Attribute` IA on AV.parent = IA.name where IA.numeric_values =0 and IA.attribute_name = 'Unit For' order by AV.attribute_value asc""", as_dict=1)
	context["search_unit_for_item"] = [d for d in unit_for]
	
	unit_type = frappe.db.sql("""\
	select AV.attribute_value, AV.name from `tabItem Attribute Value` AV inner join `tabItem Attribute` IA on AV.parent = IA.name where IA.numeric_values =0 and IA.attribute_name = 'Property Type' order by AV.attribute_value asc""", as_dict=1)
	context["search_unit_type_item"] = [d for d in unit_type]
	
	unit_finishing = frappe.db.sql("""\
	select AV.attribute_value, AV.name from `tabItem Attribute Value` AV inner join `tabItem Attribute` IA on AV.parent = IA.name where IA.numeric_values =0 and IA.attribute_name = 'Property Finishing' order by AV.attribute_value asc""", as_dict=1)
	context["search_unit_finishing_item"] = [d for d in unit_finishing]
	
	projects_name = frappe.db.sql("""\
	select IG.item_group_name from `tabItem Group` IG inner join `tabItem` I on IG.item_group_name = I.item_group where IG.is_group = 0 and IG.show_in_website = 1 group by IG.item_group_name order by IG.item_group_name asc""", as_dict=1)
	context["search_unit_projects_item"] = [d for d in projects_name]
	
	room_number = frappe.db.sql("""\
	select IA.numeric_values,IA.from_range,IA.increment,IA.to_range from `tabItem Attribute` IA  where IA.attribute_name = 'Rooms' """, as_dict=1)
	context["search_room_number"] = [d for d in room_number]
	
	unit_area = frappe.db.sql("""\
	select IA.numeric_values,IA.from_range,IA.increment,IA.to_range from `tabItem Attribute` IA  where IA.attribute_name = 'Area' """, as_dict=1)
	context["search_unit_area"] = [d for d in unit_area]
	
	
	
	
	context["propertiesLocation"] = frappe.form_dict.get("location")
	context["propertiesunit_usage"] = frappe.form_dict.get("usage")
	context.update({
			"items": get_units_list(),
			"products_as_list": cint(frappe.db.get_single_value('Website Settings', 'products_as_list'))
		})
	
	return context

@frappe.whitelist(allow_guest=True)
def get_units_list():
	# limit = 12 because we show 12 items in the grid view

	# base query
	query = """select I.has_variants,I.variant_of,I.territory,I.unit_usage,I.name, I.item_name, I.item_code, I.route, I.image, I.website_image, I.thumbnail, I.item_group,
			I.description, I.web_long_description as website_description, I.is_stock_item,
			case when (S.actual_qty - S.reserved_qty) > 0 then 1 else 0 end as in_stock, I.website_warehouse,
			I.has_batch_no,IT.route as variantroute
		from `tabItem` I
		left join tabItem IT on IT.item_code = I.variant_of
		left join tabBin S on I.item_code = S.item_code and I.website_warehouse = S.warehouse
		where (I.show_in_website = 1 or I.show_variant_in_website = 1)
			and I.disabled = 0
			and (I.end_of_life is null or I.end_of_life='0000-00-00' or I.end_of_life > %(today)s)"""
	if frappe.form_dict.get("location"):
		query += """ and I.territory = '{propertiesLocation}'""".format(propertiesLocation=frappe.form_dict.get("location"))
		
	if frappe.form_dict.get("usage"):
		query += """ and I.unit_usage = '{propertiesunit_usage}'""".format(propertiesunit_usage=frappe.form_dict.get("usage"))

	# order by
	query += """ order by I.weightage desc, in_stock desc, I.modified desc """ 

	data = frappe.db.sql(query, {"today": nowdate()}, as_dict=1)
	#for item in data:
	#	if item["variant_of"]
	#		set_product_route_info_for_website(item)
		
	return [r for r in data]
	

def set_product_route_info_for_website(item):
	"""set product price uom for website"""
	product_info = get_product_info_for_website(item.item_code)

	if product_info:
		item.update(product_info)
		item["stock_uom"] = product_info.get("uom")
		item["sales_uom"] = product_info.get("sales_uom")
		if product_info.get("price"):
			item["price_stock_uom"] = product_info.get("price").get("formatted_price")
			item["price_sales_uom"] = product_info.get("price").get("formatted_price_sales_uom")
		else:
			item["price_stock_uom"] = ""
			item["price_sales_uom"] = ""
	
def get_product_list(search=None, start=0, limit=12):
	# limit = 12 because we show 12 items in the grid view

	# base query
	query = """select I.territory,I.unit_usage,I.name, I.item_name, I.item_code, I.route, I.image, I.website_image, I.thumbnail, I.item_group,
			I.description, I.web_long_description as website_description, I.is_stock_item,
			case when (S.actual_qty - S.reserved_qty) > 0 then 1 else 0 end as in_stock, I.website_warehouse,
			I.has_batch_no
		from `tabItem` I
		left join tabBin S on I.item_code = S.item_code and I.website_warehouse = S.warehouse
		where (I.show_in_website = 1 or I.show_variant_in_website = 1)
			and I.disabled = 0
			and (I.end_of_life is null or I.end_of_life='0000-00-00' or I.end_of_life > %(today)s)"""
	if frappe.form_dict.get("location"):
		query += """ and I.territory = '{propertiesLocation}'""".format(propertiesLocation=frappe.form_dict.get("location"))
		
	if frappe.form_dict.get("usage"):
		query += """ and I.unit_usage = '{propertiesunit_usage}'""".format(propertiesunit_usage=frappe.form_dict.get("usage"))
		
	# search term condition
	if search:
		query += """ and (I.web_long_description like %(search)s
				or I.description like %(search)s
				or I.item_name like %(search)s
				or I.name like %(search)s)"""
		search = "%" + cstr(search) + "%"

	# order by
	query += """ order by I.weightage desc, in_stock desc, I.modified desc """ 

	data = frappe.db.sql(query, {
		"search": search,
		"today": nowdate()
	}, as_dict=1)

	for item in data:
		set_product_info_for_website(item)

	return [get_item_for_list_in_html(r) for r in data]

@frappe.whitelist(allow_guest=True)
def get_projects_list():
	unit_projects = frappe.db.sql("""\
	select  IG.item_group_name `tabItem Group` IG where IG.show_in_website =1 order by IG.item_group_name asc""", as_dict=1)

	return [d for d in unit_projects]

