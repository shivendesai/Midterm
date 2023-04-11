#Written by Shiven Desai
# Create a 2-D list with the numbers 1-10
numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# Retrieve the number 7 from the list
lucky_number = None
for row in numbers:
    if 7 in row:
        lucky_number = row[row.index(7)]
        break

# Print the result
print(f"Lucky number: {lucky_number}")