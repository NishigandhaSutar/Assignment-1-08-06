#student marks calculation

print("Enter 5 subjects: ")
sub1=input("Enter subject 1: ")
sub2=input("Enter subject 2: ")
sub3=input("Enter subject 3: ")
sub4=input("Enter subject 4: ")
sub5=input("Enter subject 5: ")

mrk1=float(input(f"Enter marks for {sub1}: "))
mrk2=float(input(f"Enter marks for {sub2}: "))
mrk3=float(input(f"Enter marks for {sub3}: "))
mrk4=float(input(f"Enter marks for {sub4}: "))
mrk5=float(input(f"Enter marks for {sub5}: "))

Total=mrk1+mrk2+mrk3+mrk4+mrk5
print(Total)
Average_marks=Total/5
print("Average Marks: ",Average_marks)
print("Percentage:",(Total/500*100))


