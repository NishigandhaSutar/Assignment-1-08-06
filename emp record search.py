# this is employee record search system
employees = ["TukTuk", "BakBak", "innocent", "bestie","serious"]

name = input("Enter employee name: ")

if name in employees:
    print("Employee Found")
else:
    print("Employee Not Found")