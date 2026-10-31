def generate_payroll(emp_name, basic, ot_hours, incentive):
    hra = 0.20 * basic
    da = 0.10 * basic
    ot_pay = ot_hours * 200.0
    gross = basic + hra + da + ot_pay + incentive
    
    pf = 0.12 * basic
    if gross <= 50000:
        tax = 0.0
    elif gross <= 100000:
        tax = 0.10 * (gross - 50000)
    else:
        tax = (50000 * 0.10) + ((gross - 100000) * 0.20)
        
    total_deductions = pf + tax
    net_salary = gross - total_deductions
    
    return gross, total_deductions, net_salary

employees = [
    ("Vikram", 40000, 10, 3000),
    ("Neha", 75000, 5, 5000),
    ("Suresh", 120000, 0, 10000)
]

print("--- Corporate Employee Salary Statement ---")
for emp in employees:
    gross, ded, net = generate_payroll(emp[0], emp[1], emp[2], emp[3])
    print(f"Emp: {emp[0]:<8} | Gross: ₹{gross:<10.2f} | Deductions: ₹{ded:<8.2f} | Net: ₹{net:<10.2f}")