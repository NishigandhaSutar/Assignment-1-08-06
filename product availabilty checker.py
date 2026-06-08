#this is product availability check
products = ["Atomic habits", "ikigai", "the secret", "mountain is you"]

item = input("Enter product name: ")

if item in products:
    print("Product is available")
else:
    print("Product is not available")