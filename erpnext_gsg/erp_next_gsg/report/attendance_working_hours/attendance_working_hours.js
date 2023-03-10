// Copyright (c) 2023, Mohammed AlShanti and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
	{ fieldname: 'from_date', label: __('From Date'), fieldtype: 'Date'},
	{ fieldname: 'to_date', label: __('To Date'), fieldtype: 'Date'},
	{ fieldname: 'employee', label: __('Employee'), fieldtype: 'Link', options: 'Employeee' },
	{ fieldname: 'department', label: __('Department'), fieldtype: 'Link', options: 'Department' },
	]
};
