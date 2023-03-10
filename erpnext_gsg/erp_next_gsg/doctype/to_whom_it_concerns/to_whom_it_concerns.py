# Copyright (c) 2023, Mohammed AlShanti and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ToWhomItConcerns(Document):
	def validate(self):
		query = frappe.db.sql(f""" select net_pay from `tabSalary Slip`
		where employee = '{self.employee}' order by name desc""")[0][0]
		self.salary = query
