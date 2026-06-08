#salary calculation system

basic = float(input("Enter Basic Salary: "))

hra_percent = float(input("Enter HRA Percentage: "))
da_percent = float(input("Enter DA Percentage: "))
ded_percent = float(input("Enter Deduction Percentage: "))
#calculating hra and dra
hra = (basic * hra_percent) / 100
da = (basic * da_percent) / 100
#calculating gross salary
gross = basic + hra + da

deduction = (gross * ded_percent) / 100

net = gross - deduction

print("\nGross Salary =", gross)
print("Deduction =", deduction)
print("Net Salary =", net)