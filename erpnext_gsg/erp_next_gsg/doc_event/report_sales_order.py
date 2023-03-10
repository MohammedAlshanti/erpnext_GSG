import frappe
from frappe import _
from erpnext.accounts.report.sales_order_analysis.sales_order_analysis import SalesOrderAnalysis

def sales_order_analysis_filter(self):
    filters = self.get_filters()
    from_time = filters.get('from_time')
    to_time = filters.get('to_time')

    if not from_time:
        frappe.throw(_('From Time is mandatory'))

    if not to_time:
        frappe.throw(_('To Time is mandatory'))

    return {'from_time': from_time, 'to_time': to_time}

SalesOrderAnalysis.get_filters = sales_order_analysis_filter














