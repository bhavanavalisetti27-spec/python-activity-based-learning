def generate_retail_invoice(cart):
    tax_rates = {"Electronics": 0.18, "Grocery": 0.05, "Clothing": 0.12}
    
    subtotal = 0.0
    total_tax = 0.0
    invoice_items = []
    
    for item, qty, price, category in cart:
        base_cost = qty * price
        rate = tax_rates.get(category, 0.0)
        tax = base_cost * rate
        
        subtotal += base_cost
        total_tax += tax
        invoice_items.append((item, qty, base_cost, tax))
        
    gross_total = subtotal + total_tax
    
    # Cart Threshold Discount
    if gross_total > 5000:
        discount = min(1000.0, gross_total * 0.10)
    else:
        discount = 0.0
        
    final_payable = gross_total - discount
    return invoice_items, gross_total, discount, final_payable

# Sample Cart: (Name, Qty, Unit Price, Category)
shopping_cart = [
    ("Laptop Bag", 1, 2500, "Clothing"),
    ("Wireless Mouse", 2, 1200, "Electronics"),
    ("Organic Oats", 4, 300, "Grocery")
]

items_summary, gross, disc, final_amt = generate_retail_invoice(shopping_cart)

print("--- RETAIL STORE TAX INVOICE ---")
for it in items_summary:
    print(f"Item: {it[0]:<15} | Qty: {it[1]:<2} | Base: ₹{it[2]:<8.2f} | Tax: ₹{it[3]:<6.2f}")
print("-" * 50)
print(f"Gross Amount (Incl. Tax): ₹{gross:.2f}")
print(f"Discount Applied        : -₹{disc:.2f}")
print(f"Final Amount Payable    : ₹{final_amt:.2f}")