# Employee Bonous eligibility
#Attendeance based bonus system -

num=int(input("Enter the number of employees: "))

for i in range(num):
    name = input(f"Enter the name of employee {i + 1}: ")
    att=float(input(f"Enter the attendanec of {name}: "))

    if att>90:
        print(f" Employee {name} is eligible for bonous")
    else:
        print(f" Employee {name} is not eligible for bonous")


