# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

from hendaza_custom_site.hendaza_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details


def get_context(context):
	doc = frappe.get_doc("Website Contact Us Settings", "Website Contact Us Settings")

	if doc.query_options:
		query_options = [opt.strip() for opt in doc.query_options.replace(",", "\n").split("\n") if opt]
	else:
		query_options = ["Sales", "Support", "General"]

	out = {
		"query_options": query_options,
		"no_page_content": 1,
		"title": doc.heading or "",
		"light_description": doc.light_description or "",
		"parents": [
			{ "name": _("Home"), "route": "/" }
		]
	}
	out.update(doc.as_dict())
	if doc.page_header_background:
		out.update(get_website_header_background_details(doc.page_header_background))
	return out

max_communications_per_hour = 1000

@frappe.whitelist(allow_guest=True)
def send_message(sendername="",subject="Website Query", message="", sender=""):
	if not message:
		frappe.response["message"] = 'Please write something'
		return

	if not sender:
		frappe.response["message"] = 'Email Address Required'
		return
		
	if not sendername:
		frappe.response["message"] = 'Name Required'
		return

	# guest method, cap max writes per hour
	if frappe.db.sql("""select count(*) from `tabCommunication`
		where `sent_or_received`="Received"
		and TIMEDIFF(%s, modified) < '01:00:00'""", now())[0][0] > max_communications_per_hour:
		frappe.response["message"] = "Sorry: we believe we have received an unreasonably high number of requests of this kind. Please try later"
		return

	# send email
	forward_to_email = frappe.db.get_value("Contact Us Settings", None, "forward_to_email")
	if forward_to_email:
		frappe.sendmail(recipients=forward_to_email, sender=sender, content=message, subject=subject)


	# add to to-do ?
	frappe.get_doc(dict(
		doctype = 'Communication',
		sender=sender,
		subject= _('New Message from Website Contact Page'),
		sent_or_received='Received',
		content=message,
		status='Open',
	)).insert(ignore_permissions=True)

	return "okay"
