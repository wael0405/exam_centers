// Copyright (c) 2024, Wael Al-edrisi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reservation', {
	// refresh: function(frm) {

	// },

	university: function(frm){
		frm.set_query("college" , function(){
			return {
				"filters":{
					"university":frm.doc.university
				}
			};
		});
	},
	college: function(frm){
		frm.set_query("major" , function(){
			return {
				"filters":{
					"college":frm.doc.college
				}
			};
		});
	},
	major: function(frm){
		frm.set_query("level" , function(){
			return {
				"filters":{
					"major":frm.doc.major
				}
			};
		});
	},
	major: function(frm){
		frm.set_query("subject" , function(){
			return {
				"filters":{
					"major":frm.doc.major,
					"level":frm.doc.level,
					"semester":frm.doc.semester
				}
			};
		});
	},
	college: function(frm){
		frm.set_query("major" , function(){
			return {
				"filters":{
					"college":frm.doc.college
				}
			};
		});
	},


});
