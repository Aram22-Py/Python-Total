#Day 2 project: Comissions calculator
print("Hello! If you would like to calculate the amount of your commissions, please enter your full name and the number of sales for the month.")
full_name = input("Enter your full name: ")
number_of_sales = input("Enter the number of sales for the month: ")
calculated_commission = int(number_of_sales) * (13/100)

print(f"Name: {full_name}\nNumber of sales: {number_of_sales}")
print(f"The commission you are entitled to is: {round(calculated_commission, 2)}\nThank you for using our services.")
