def compute_electricity_bill(units):
    fixed_charge = 150.0
    energy_charge = 0.0
    
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 300:
        energy_charge = (100 * 3.0) + ((units - 100) * 5.0)
    else:
        energy_charge = (100 * 3.0) + (200 * 5.0) + ((units - 300) * 8.0)
        
    total = fixed_charge + energy_charge
    
    # Rebate/Surcharge
    if units <100:
        total -= total * 0.02
    if total > 2000:
        total += total * 0.05
        
    return total

months = ["Jan", "Feb", "Mar", "Apr", "May"]
monthly_units = [80, 120, 250, 350, 200]
previous_units = None

print("--- Progressive Monthly Billing Report ---")
for i in range(len(months)):
    units = monthly_units[i]
    bill = compute_electricity_bill(units)
    flag = ""
    
    if previous_units is not None:
        increase = ((units - previous_units) / previous_units) * 100
        if increase >= 30:
            flag = f"ALERT: Unusual Increase ({increase:.1f}%)"
            
    print(f"Month: {months[i]:<5} | Units: {units:<4} | Bill: ₹{bill:<8.2f} | {flag}")
    previous_units = units