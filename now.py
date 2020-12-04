total_cost_of_home = input("whats the cost of your dream house price: ")
annual_salary = float(input("enter your annual salary: "))
portion_saved = float(input("how much do u want to save: "))
monthly_salary = annual_salary/12
current_savings = 0
portion_down_payment = 0.25 * float(total_cost_of_home)
savings = 0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    savings = current_savings * r/12
    current_savings = current_savings + savings + (portion_saved * monthly_salary)
    months += 1
print("the number of month will be: " + str(months))


