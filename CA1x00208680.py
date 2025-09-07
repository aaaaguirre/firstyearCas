# Qa

# inputs
tour_code = input("Enter your tour code:")
no_of_customers = int(input("Enter number of customers:"))

# variables
CUSTOMER_BONUS = 0.05
tour = 100
tour_profit = 0
congestion_charge = 0.10

# Qc
tour_hours = 4.26
tour_minutes = 256

# processing

if no_of_customers < 20:
    tour_profit = tour * 10 * no_of_customers

elif no_of_customers == 50:
    # 20-50 incl
    tour_profit = tour * 15 * no_of_customers

elif no_of_customers > 50:
    tour_profit = tour * 20 * no_of_customers + CUSTOMER_BONUS
    print("You owe a 5% bonus")

# Qb

else:
    print("Invalid Number or Tour Code (CYT XXX): ")

total_profit = tour_profit * congestion_charge


# outputs

print("Tour profit:", tour_profit)
print("Net profit:", round(total_profit, 2))
print("Amount of congestion charge paid:", round(congestion_charge, 2))
print("Hour duration:", tour_hours, "hours")
print("Minute duration:", tour_minutes, "minutes")




