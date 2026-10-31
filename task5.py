def optimize_telecom_plan(total_data_gb, total_call_mins):
    days = 28
    plans = [
        {"name": "Plan A", "rental": 299, "data_limit": 1.5 * days, "call_limit": 99999, "data_rate": 10, "call_rate": 0},
        {"name": "Plan B", "rental": 399, "data_limit": 2.0 * days, "call_limit": 99999, "data_rate": 8, "call_rate": 0},
        {"name": "Plan C", "rental": 199, "data_limit": 1.0 * days, "call_limit": 100 * days, "data_rate": 15, "call_rate": 0.50}
    ]
    
    best_plan = None
    min_cost = float('inf')
    results = []
    
    for p in plans:
        extra_data = max(0.0, total_data_gb - p["data_limit"])
        extra_calls = max(0.0, total_call_mins - p["call_limit"])
        
        cost = p["rental"] + (extra_data * p["data_rate"]) + (extra_calls * p["call_rate"])
        results.append((p["name"], cost))
        
        if cost < min_cost:
            min_cost = cost
            best_plan = p["name"]
            
    return results, best_plan, min_cost

user_data = 50.0  # GB
user_calls = 3000  # Mins

costs, best, lowest = optimize_telecom_plan(user_data, user_calls)

print(f"--- Telecom Plan Recommendation (Usage: {user_data}GB, {user_calls} Mins) ---")
for plan_name, cost in costs:
    print(f"Plan: {plan_name:<8} | Total Monthly Cost: ₹{cost:.2f}")
print(f"\nRecommended Optimal Plan: {best} with Cost ₹{lowest:.2f}")