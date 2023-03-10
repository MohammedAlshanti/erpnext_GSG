frappe.provide('erpnext.accounts.report');

erpnext.accounts.report.SalesOrderAnalysis = erpnext.accounts.report.SalesOrderAnalysis.extend({
    get_filters: function () {
        var filters = this._super();
        filters.from_time = this.$wrapper.find('[name="from_time"]').val();
        filters.to_time = this.$wrapper.find('[name="to_time"]').val();
        return filters;
    }
});
frappe.ui.form.on('Sales Order', {
    onload: function (frm) {
        frm.set_query('sales_order_time', function () {
            return {
                filters: {
                    'docstatus': 1
                }
            };
        });
    }
});
