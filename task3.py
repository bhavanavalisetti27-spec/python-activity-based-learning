def process_patient_billing(patient_id, name, diag_cost, treat_cost, category):
    consultation_fee = 500.0
    subtotal = consultation_fee + diag_cost + treat_cost
    
    if category == "BPL":
        discount = 0.50 * subtotal
    elif category == "Senior Citizen":
        discount = 0.20 * subtotal
    else:
        discount = 0.0
        
    net = subtotal - discount
    
    if category == "General" and net > 10000:
        net += net * 0.05  # Service charge
        
    # Classification
    if category == "BPL":
        classification = "Subsidized Care"
    elif net > 15000:
        classification = "High-Value Account"
    else:
        classification = "Standard Account"
        
    return net, classification

# Sample Patients
patients = [
    ("P101", "Ramesh", 4500, 12000, "General"),
    ("P102", "Sita", 3000, 8000, "Senior Citizen"),
    ("P103", "Aman", 5000, 15000, "BPL")
]

print("--- Hospital Patient Billing Summary ---")
for p in patients:
    net_payable, cls = process_patient_billing(p[0], p[1], p[2], p[3], p[4])
    print(f"ID: {p[0]} | Name: {p[1]:<8} | Category: {p[4]:<14} | Net: ₹{net_payable:<9.2f} | Class: {cls}")