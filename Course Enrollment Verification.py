# this is Course Enrollment Verification system
courses = ["Python", "Java", "Web Development", "Data Science","Arudino"]

course = input("Enter course name: ")

if course in courses:
    print("Course is available")
else:
    print("Course is not available")

course_students = ["Tuktuk", "bakbak", "innocent", "bestie","serious"]

name = input("Enter student name: ")

if name in course_students:
    print("Student is enrolled in the course")
else:
    print("Student is not enrolled in the course")

