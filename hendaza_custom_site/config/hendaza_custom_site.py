from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Web Site"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Web Page",
					"description": _("Content web page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Slideshow",
					"description": _("Embed image slideshows in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Header Background",
					"description": _("Embed image header background in website pages."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Route Meta",
					"description": _("Add meta tags to your web pages"),
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Website Settings",
					"description": _("Setup of top navigation bar, footer and logo."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Hendaza Website Settings",
					"description": _("Setup site Language."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Homepage",
					"description": _("Settings for website home page"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website About Us Settings",
					"description": _("Settings for About Us Page."),
				},
				{
					"type": "doctype",
					"name": "Website Contact Us Settings",
					"description": _("Settings for Contact Us Page."),
				},
				{
					"type": "doctype",
					"name": "Coming Soon Settings",
					"description": _("Settings for Coming Soon Page."),
				},
				
			]
		},
		{
			"label": _("Property Settings"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Item",
				},
				{
					"type": "doctype",
					"name": "Item Group",
					"icon": "fa fa-sitemap",
					"label": _("Item Group"),
					"link": "Tree/Item Group",
				},
				{
					"type": "doctype",
					"name": "Item Attribute",
				},
				{
					"type": "doctype",
					"name": "Property Features",
					"description": _("Set property features items."),
				},
				{
					"type": "doctype",
					"name": "Unit Usage",
					"description": _("Set unit usage type."),
				},				
			]
		},

	]