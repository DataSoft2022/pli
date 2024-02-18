import frappe

#####DONE#####
@frappe.whitelist()
def get_item(serial_no):
    data = frappe.db.sql("""
        SELECT
            se.name
        FROM
            `tabStock Entry` se
        INNER JOIN
            `tabStock Entry Detail` sed
        ON
            se.name = sed.parent
        WHERE
            se.stock_entry_type = 'Manufacture'
            AND sed.serial_and_batch_bundle = %s
        """, (serial_no), as_dict=1)
    name = data[0]['name']
    data = frappe.get_all(
        doctype="Stock Entry Detail",
        filters={"parent": name},
        fields=["item_code", "valuation_rate", "set_basic_rate_manually" , "basic_amount" , "basic_rate"]
    )
    return data