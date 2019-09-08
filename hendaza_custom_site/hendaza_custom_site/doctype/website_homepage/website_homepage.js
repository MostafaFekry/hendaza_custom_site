// Copyright (c) 2019, MostafaFekry and contributors
// For license information, please see license.txt

frappe.ui.form.on('Website Homepage', {
	setup: function(frm) {
		frm.fields_dict["homepage_items_group"].grid.get_field("item_group_name").get_query = function(){
			return {
				filters: {'show_in_website': 1,'is_group': 0}
			}
		},
		frm.fields_dict["homepage_products_items"].grid.get_field("item_code").get_query = function(){
			return {
				filters: {'show_in_website': 1}
			}
		}
	},
	refresh: function(frm) {

	}
});