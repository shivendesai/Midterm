#Written by Shiven Desai
# Create a 1-D list with the numbers 20-30
numbers = list(range(20, 31))

# Retrieve the number 27 from the list
lucky_number = numbers[numbers.index(27)]

# Print the result
print(f"Lucky number: {lucky_number}")