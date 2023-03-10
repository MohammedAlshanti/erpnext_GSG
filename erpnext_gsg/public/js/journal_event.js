frappe.ui.form.on('Journal Entry', {
    refresh: function(frm) {
        cur_frm.set_df_property('voucher_type', 'options', ['Journal Entry', 'Bank Entry', 'Cash Entry', 'Cash Entry', 'Credit Card Entry', 'Debit Note', 'Credit Note', 'Contra Entry', 'Excise Entry', 'Write Off Entry', 'Opening Entry', 'Depreciation Entry', 'Exchange Rate Revaluation', 'Deferred Revenue']);
    }
});