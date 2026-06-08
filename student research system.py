#this is student research system
students = ["Tuktuk", "bakbak", "inoccent", "bestie","serious"]

name = input("Enter student name: ")

if name in students:
    print("Student found")
else:
    print("Student not found")