# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_request_site_address, encode
from frappe.model.document import Document
from hendaza_custom_site.hendaza_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

def update_website_context(context):
	context["mostafa_test"] = frappe.form_dict._lang
	website_languages_request = frappe.form_dict._lang
	if website_languages_request:
		context["website_languages_request"] = website_languages_request
	else:
		context["website_languages_request"] = "en"
		website_languages_request = "en"
	
	
	context["website_languages_items"] = get_website_languages_items()
	context.update(get_website_languages_details(website_languages_request))
	
	website_settings = frappe.get_doc('Hendaza Website Settings')
	context["enable_multilanguage_support"] = website_settings.enable_multilanguage_support
	context["display_language_picker_in_top_bar"] = website_settings.display_language_picker_in_top_bar
	
	
	if website_settings.page_header_background:
		context.update(get_website_header_background_details(website_settings.page_header_background))

	context["facebook_link"] = website_settings.facebook_link
	context["linked_in_link"] = website_settings.linked_in_link
	context["twitter_link"] = website_settings.twitter_link
	context["instagram_link"] = website_settings.instagram_link
	context["google_link"] = website_settings.google_link
	
	# Mostafa return filter location data
	context["item_group_filter_location"] = get_location_territory()
		
	#  Mostafa return filter unit usage data
	context["item_group_filter_unit_usage"] = get_unit_usage()
	

def get_location_territory():
	
	territory_name = frappe.db.sql("""\
	select T.territory_name, T.name from `tabTerritory` T inner join `tabItem Group` I on T.name = I.territory and I.show_in_website = 1 and I.docstatus = 0 where T.is_group =0 group by T.territory_name order by T.territory_name asc""", as_dict=1)

	territory_name_item = [d for d in territory_name]
	
	return territory_name_item

def get_unit_usage():
	
	unit_usage = frappe.db.sql("""\
	select UU.unit_usage, UU.name from `tabUnit Usage` UU inner join `tabItem Group` I on UU.name = I.unit_usage and I.docstatus = 0 group by UU.unit_usage order by UU.unit_usage asc""", as_dict=1)

	unit_usage_item = [d for d in unit_usage]
	
	return unit_usage_item
	
def get_website_languages_items():
	all_language_items = frappe.db.sql("""\
		select * from `tabWebsite Languages`
		where parent='Hendaza Website Settings' 
		order by idx asc""", as_dict=1)
	if all_language_items:
		website_languages_items = [d for d in all_language_items]
	else:
		website_languages_items = []
	return website_languages_items
	
def get_website_languages_details(website_languages_request="en"):
	website_languages_details = frappe.get_doc("Website Languages", website_languages_request)
	if not website_languages_details:
		return {}

	return {
		"website_languages_name": website_languages_details.language_name,
		"website_languages_flag": website_languages_details.language_flag,
		"banner_lang_html": website_languages_details.banner_lang_html,
		"slogan": website_languages_details.slogan,
		"newsletter_title": website_languages_details.newsletter_title,
		"newsletter_description": website_languages_details.newsletter_description,
		"newsletter_success_message": website_languages_details.newsletter_success_message,
		"newsletter_field": website_languages_details.newsletter_field,
		"newsletter_button": website_languages_details.newsletter_button,
		"social_tab_title": website_languages_details.social_tab_title,
		"contact_us_tab_title": website_languages_details.contact_us_tab_title,
		"contact_us_address": website_languages_details.contact_us_address,
		"contact_us_hotline": website_languages_details.contact_us_hotline,
		"contact_us_phone": website_languages_details.contact_us_phone,
		"contact_us_email": website_languages_details.contact_us_email,
		"footer_logo_code": website_languages_details.footer_logo_code,
		"website_languages_copyright": website_languages_details.copyright
	}

@frappe.whitelist(allow_guest=True)
def create_lead_for_item_inquiry(lead,mobile,email, subject, message,company=None):

	lead_doc = frappe.new_doc('Lead')
	lead_doc.lead_name = lead
	if company:
		lead_doc.company_name = company
	lead_doc.mobile_no = mobile
	lead_doc.email_id = email
	lead_doc.status = 'Lead'
	lead_doc.lead_owner = ''
	
	try:
		lead_doc.insert(ignore_permissions=True)
		lead_doc.save(ignore_permissions=True)
	except frappe.exceptions.DuplicateEntryError:
		frappe.clear_messages()
		lead_doc = frappe.get_doc('Lead', {'email_id': email})

	lead_doc.add_comment('Comment', text='''
		<div>
			<h5>{subject}</h5>
			<p>{message}</p>
		</div>
	'''.format(subject=subject, message=message))

	return "okay"