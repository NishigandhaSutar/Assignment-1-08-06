# This is Library Book Search system
books = ["English", "Korean", "Italian", "French","Hindi"]

book = input("Enter book name: ")

if book in books:
    print("Book available in library")
else:
    print("Book not available")