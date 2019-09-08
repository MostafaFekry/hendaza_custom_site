# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	doc = frappe.get_doc('Coming Soon Settings','Coming Soon Settings')
	
	out = {
		"homedescription": doc.description,
		"homecontent": doc.content,
		"title": doc.title or "Coming Soon",
		"image": doc.image or "",
		"allow_subscribe": doc.allow_subscribe,
		"subscribe_title": doc.subscribe_title,
		"subscribe_header": doc.subscribe_header,
		"subscribe_description": doc.subscribe_description
	}
	out.update(doc.as_dict())
	return out


