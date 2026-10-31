def analyze_travel_budget(budget_inr, expense_records):
    rates = {"USD": 83.0, "EUR": 90.0, "GBP": 105.0, "INR": 1.0}
    conversion_fee_rate = 0.025
    
    total_spent_inr = 0.0
    highest_cost = 0.0
    largest_category = ""
    
    print("--- Foreign Expense Itemized Log (in INR) ---")
    for category, amount, currency in expense_records:
        rate = rates.get(currency, 1.0)
        base_inr = amount * rate
        fee = base_inr * conversion_fee_rate
        total_cost = base_inr + fee
        
        total_spent_inr += total_cost
        
        if total_cost > highest_cost:
            highest_cost = total_cost
            largest_category = category
            
        print(f"Cat: {category:<12} | {amount:>7.2f} {currency:<3} -> ₹{total_cost:<10.2f} (Incl. Fee)")
        
    balance = budget_inr - total_spent_inr
    return total_spent_inr, balance, largest_category

trip_budget = 150000.0  # INR
expenses = [
    ("Lodging", 900, "USD"),
    ("Dining", 350, "EUR"),
    ("Transport", 100, "GBP"),
    ("Excursions", 200, "USD")
]

spent, remaining, peak_cat = analyze_travel_budget(trip_budget, expenses)

print("-" * 55)
print(f"Total Trip Cost     : ₹{spent:.2f}")
print(f"Budget Remaining    : ₹{remaining:.2f}")
print(f"Largest Expense Area: {peak_cat}")
if remaining < 0:
    print("WARNING: Budget Exceeded!")