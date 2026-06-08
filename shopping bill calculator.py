#shopping bill calculator
num=int(input("Enter the number of items: "))
bill=0
for i in range(num):
    item = input(f"Enter the item {i + 1}: ")
    price=float(input(f"Enter the price of {item}: "))
    bill+=price
print(f"Total Bill: {bill}")

