#Written by Shiven Desai
# Prompt the user to enter their expenses for each category
rent = input("Enter your rent expense: ")
gas = input("Enter your gas expense: ")
food = input("Enter your food expense: ")
clothing = input("Enter your clothing expense: ")
car_payment = input("Enter your car payment expense: ")

# Open the expenses.txt file in write mode
with open("expenses.txt", "w") as file:
    # Write the expenses to the file
    file.write(f"Rent: {rent}\n")
    file.write(f"Gas: {gas}\n")
    file.write(f"Food: {food}\n")
    file.write(f"Clothing: {clothing}\n")
    file.write(f"Car Payment: {car_payment}\n")

# Open the expenses.txt file in read mode
with open("expenses.txt", "r") as file:
    # Read the contents of the file
    data = file.read()
    # Print the contents of the file
    print(data)