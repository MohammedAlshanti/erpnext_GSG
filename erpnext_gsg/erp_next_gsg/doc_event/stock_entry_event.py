import frappe

def create_stock_entry(doc, method):
    if doc.purpose == 'Material Issue':
        stock_entry = frappe.new_doc('Stock Entry')
        stock_entry.stock_entry_type = 'Material Issue'
        stock_entry.to_warehouse = doc.requested_for_warehouse
        for item in doc.items:
            stock_entry.append('items', {
                'item_code': item.item_code,
                'qty': item.qty,
            })
        stock_entry.save(ignore_permissions=True)
        stock_entry.insert()
        stock_entry.submit()
