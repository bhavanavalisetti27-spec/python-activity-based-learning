def calculate_railway_fare(distance_km, travel_class, passengers):
    class_multipliers = {"Sleeper": 1.0, "3AC": 2.5, "2AC": 3.5, "1AC": 5.0}
    reservation_fee = 40.0
    
    mult = class_multipliers.get(travel_class, 1.0)
    base_fare = distance_km * 0.50 * mult
    
    total_fare = 0.0
    details = []
    
    for name, age in passengers:
        if age < 12:
            discount = 0.50
        elif age >= 60:
            discount = 0.40
        else:
            discount = 0.0
            
        p_fare = (base_fare * (1.0 - discount)) + reservation_fee
        total_fare += p_fare
        details.append((name, age, p_fare))
        
    return total_fare, details

passengers_list = [("Rajesh", 45), ("Sunita", 62), ("Rohan", 8)]
dist = 750  # km
t_class = "3AC"

total, breakdown = calculate_railway_fare(dist, t_class, passengers_list)

print(f"--- Railway Reservation Summary ({dist} km, Class: {t_class}) ---")
for b in breakdown:
    print(f"Passenger: {b[0]:<10} | Age: {b[1]:<3} | Fare: ₹{b[2]:.2f}")
print(f"Total Reservation Fare: ₹{total:.2f}")