// Copyright (c) 2019, MostafaFekry and contributors
// For license information, please see license.txt

frappe.ui.form.on('Website Contact Us Settings', {
	refresh: function(frm) {
		frm.sidebar.add_user_action(__("See on Website")).attr("href", "/contactus").attr("target", "_blank");
	}
});
