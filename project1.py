#Written by Shiven Desai
# Define a function to calculate the number of calories from fat
def calories_from_fat(fat_grams):
    return fat_grams * 9

# Define a function to calculate the number of calories from carbohydrates
def calories_from_carbs(carb_grams):
    return carb_grams * 4

# Prompt the user to enter the number of fat grams
fat_grams = float(input("Enter the number of fat grams: "))

# Prompt the user to enter the number of carbohydrate grams
carb_grams = float(input("Enter the number of carbohydrate grams: "))

# Calculate the number of calories from fat using the defined function
calories_fat = calories_from_fat(fat_grams)

# Calculate the number of calories from carbohydrates using the defined function
calories_carbs = calories_from_carbs(carb_grams)

# Print out the results
print(f"Calories from fat: {calories_fat}")
print(f"Calories from carbohydrates: {calories_carbs}")