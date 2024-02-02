# Copyright (c) 2024, Wael Al-edrisi and contributors
# For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document

# class Reservation(Document):
# 	pass
	



from frappe.model.document import Document
import frappe
from itertools import combinations

class Reservation(Document):

    def after_insert(self):
        date = self.date
        interval = self.interval
        number_of_students = self.number_of_student

        # نطلع كل القاعات الي محجوزة في اليوم والفترة النشتي نحجزها
        reserved_halls = frappe.db.get_list('Reservation Hall',
                                            filters={'date': date, 'interval': interval},
                                            fields=['hall'])
        reserved_hall_names = [d['hall'] for d in reserved_halls]

        available_halls = frappe.db.get_list('Exam Hall',
                                             filters={
                                                 'name': ['not in', reserved_hall_names],
                                                 'status': 'متاح'
                                             },
                                             fields=['name', 'number_of_devices'])

        
        available_halls.sort(key=lambda h: h['number_of_devices'], reverse=True)

        
        selected_halls = []

        # شلس امع القاعات لما اوصل لعدد مقاعد يكفي الطلاب
        devices_accumulated = 0
        for hall in available_halls:
            devices_accumulated += hall['number_of_devices']
            selected_halls.append(hall)
            if devices_accumulated >= number_of_students:
                break 

       
        if devices_accumulated < number_of_students:
            frappe.throw("لايود مقاعد كافية لعدد الطلاب المحدد ,الرجاء القيام بتغيير الفترة أو اليوم ")

        # If a valid combination is found, create Reservation Hall records
        for hall in selected_halls:
            new_reservation_hall = frappe.get_doc({
                'doctype': 'Reservation Hall',
                'reservation': self.name,
                'hall': hall['name'],
                'date': date,
                'interval': interval
            })
            new_reservation_hall.flags.ignore_permissions = True
            new_reservation_hall.insert()





