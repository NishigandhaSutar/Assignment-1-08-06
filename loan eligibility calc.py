#loan eligibility checker
print("Welcome to the Loan Eligibility Calculator")
name=input("Enter your name: ")
is_jobholder=input("Do you have a job (Y/N): ")
bank_balance=float(input("Enter your bank balance: "))

if is_jobholder=="Y" and bank_balance>500000:
    print("You are eligible for loan")

else:
    print("You are not eligible for loan")

