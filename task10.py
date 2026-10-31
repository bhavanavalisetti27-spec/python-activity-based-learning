import math

def calculate_event_breakeven(venue, equipment, catering_per_head, cert_per_head, ticket_price, sponsorship):
    fixed_expenses = venue + equipment
    variable_cost_per_head = catering_per_head + cert_per_head
    
    contribution_margin = ticket_price - variable_cost_per_head
    
    if contribution_margin <= 0:
        return "Ticket price too low to cover variable costs per head."
        
    net_fixed_to_cover = fixed_expenses - sponsorship
    
    if net_fixed_to_cover <= 0:
        breakeven_attendees = 0
    else:
        breakeven_attendees = math.ceil(net_fixed_to_cover / contribution_margin)
        
    return fixed_expenses, net_fixed_to_cover, breakeven_attendees

v_cost = 25000.0
eq_cost = 15000.0
cat_head = 200.0
cert_head = 50.0
price = 350.0
sponsor = 18000.0

total_f, net_f, count = calculate_event_breakeven(v_cost, eq_cost, cat_head, cert_head, price, sponsor)

print("--- Campus Event Financial Planning ---")
print(f"Total Fixed Event Overhead : ₹{total_f:.2f}")
print(f"Sponsorship Offset Covered : ₹{sponsor:.2f}")
print(f"Net Fixed Cost Remaining   : ₹{net_f:.2f}")
print(f"Ticket Price per Head      : ₹{price:.2f}")
print(f"Variable Cost per Head     : ₹{cat_head + cert_head:.2f}")
print(f"Minimum Registrations Needed for Break-Even: {count} Students")