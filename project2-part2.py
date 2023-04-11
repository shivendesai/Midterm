#Written by Shiven Desai
# Prompt the user to enter their favorite coffee brand
coffee_brand = input("Enter your favorite coffee brand: ")

# Open the coffee.txt file in append mode
with open("coffee.txt", "a") as file:
    # Write the user's favorite coffee brand, product number, and price to the file
    file.write(f"\n{coffee_brand},99-8888,9.88")

# Open the coffee.txt file in read mode
with open("coffee.txt", "r") as file:
    # Read the contents of the file
    data = file.read()
    # Print the contents of the file
    print(data)