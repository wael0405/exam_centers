// Copyright (c) 2024, Wael Al-edrisi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Academic Year', {
	// refresh: function(frm) {

	// }

               start: function(frm) {
	   
	   //   let status ='Finished';
		 frm.set_value("status",'جاري')

	},

	end: function(frm) {
	   
	   //   let status ='Finished';
		 frm.set_value("status",'منتهي')

	},

});
