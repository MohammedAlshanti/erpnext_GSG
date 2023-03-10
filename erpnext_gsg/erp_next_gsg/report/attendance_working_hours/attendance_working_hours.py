# Copyright (c) 2023, Mohammed AlShanti and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = [],[]
	data = get_all_data(filters)
	columns = get_all_columns()
	for row in data:

			row["view_attendance"] = f'<a href="/app/attendance/{row["name"]}" target="_blank" rel="noopener">View Attendance</a>'


	return columns, data


def get_all_data(filters):

	return frappe.db.get_all('Attendance', ['name', 'attendance_date', 'employee', 'full_name', 'check_in', 'check_out', 'work_hours'], filters=filters)


def get_all_columns():
	columns = [
		{'fieldname': 'employee', 'label': _('Employee'), 'fieldtype': 'Link', 'options': 'Employeee'},
		{'fieldname': 'full_name', 'label': _('Employee Name'), 'fieldtype': 'Data'},
		{'fieldname': 'attendance_date', 'label': _('Attendance Date'), 'fieldtype': 'Date'},
		{'fieldname': 'check_in', 'label': _('Check In'), 'fieldtype': 'Time'},
		{'fieldname': 'check_out', 'label': _('Check Out'), 'fieldtype': 'Time'},
		{'fieldname': 'work_hours', 'label': _('Work Hours'), 'fieldtype': 'Float'},
		{'fieldname': 'view_attendance', 'label': _('View Attendance'), 'fieldtype': 'Data'},
	]
	return columns



