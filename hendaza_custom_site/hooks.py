# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hendaza_custom_site"
app_title = "Hendaza Custom Site"
app_publisher = "MostafaFekry"
app_description = "Custom site for Hendaza"
app_icon = "octicon octicon-globe"
app_color = "grey"
app_email = "mostafa.fekry@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hendaza_custom_site/css/hendaza_custom_site.css"
# app_include_js = "/assets/hendaza_custom_site/js/hendaza_custom_site.js"

# include js, css files in header of web template
# web_include_css = "/assets/hendaza_custom_site/css/hendaza_custom_site.css"
# web_include_js = "/assets/hendaza_custom_site/js/hendaza_custom_site.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hendaza_custom_site.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# website
update_website_context = "hendaza_custom_site.utils.update_website_context"

# before_install = "hendaza_custom_site.install.before_install"
# after_install = "hendaza_custom_site.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hendaza_custom_site.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hendaza_custom_site.tasks.all"
# 	],
# 	"daily": [
# 		"hendaza_custom_site.tasks.daily"
# 	],
# 	"hourly": [
# 		"hendaza_custom_site.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hendaza_custom_site.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hendaza_custom_site.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hendaza_custom_site.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hendaza_custom_site.event.get_events"
# }

# fixtures
fixtures = [{"dt": "Custom Field", "filters": [["name", "in", [
		"Company History-old_year",
		"Company History-title",
		"Company History-column_break_4",
		"Company History-image",
		"About Us Team Member-position",
		"Item Group-light_description",
		"Item Group-page_header_background",
		"Item Group-column_break_13",
		"Item Group-territory",
		"Item Group-unit_usage",
		"Item Group-google_maps",
		"Item Group-containssb",
		"Item Group-website_share_files",
		"Item Website Specification-property_features",
		"Item Website Specification-icon",
		"Item-light_description",
		"Item-page_header_background",
		"Item-territory",
		"Item-unit_usage",
		"Item-google_maps",
		"Item-website_share_files",
		"Item Attribute-column_break_2",
		"Item Attribute-icon",
		"Web Page-light_description",
		"Web Page-page_header_background",
		"Website Slideshow Item-slider_description",
		"Website Slideshow Item-heading_title",
		"Website Slideshow Item-column_break_5",
		"Website Slideshow Item-link_title",
		"Website Slideshow Item-link_path",
		"Website Slideshow Item-link_target",
		"Website Slideshow Item-set_position"
	]]]},
    {"dt": "Language", "filters": [["name", "in", [
		"en",
		"ar"
    ]]]},
    {"dt": "Website Languages", "filters": [["name", "in", [
		"en",
		"ar"
    ]]]},
    {"dt": "Top Bar Item"}
	]
