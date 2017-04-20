# Problem Set 1a

portion_down_payment = 0.25
current_savings = 0.0
rate = 0.04
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))
down_payment_needed = total_cost * portion_down_payment
no_months_saved = 0
previous_savings = 0.0
monthly_savings = annual_salary / 12 * portion_saved

while current_savings < down_payment_needed:
    if no_months_saved == 0:
        current_savings = monthly_savings 
    else:
        current_savings = (previous_savings * (1 + (rate / 12))) + monthly_savings
    no_months_saved += 1
    previous_savings = current_savings

print("Number of months saved: ", no_months_saved)
print("Current savings: ", current_savings)
