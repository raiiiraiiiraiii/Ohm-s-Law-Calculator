# Exercise 2: Ohm’s Law Calculator
    #Instructions:
        #1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
        #2.	Based on their choice, prompt the user to input the appropriate values.
        #3.	Use Ohm's Law to calculate the missing variable and display the result.
        #4.	Handle cases where division by zero might occur.

print("Welcome to Ohm's Law Calculator!\n")

# Ask the user what they want to calculate: Voltage, Current, or Resistance.
while True:
    try:
        calculate = int(input("What would you like to calculate?\n"
                            "1. Voltage\n"
                            "2. Current\n"
                            "3. Resistance\n"
                            "Enter here: "))
    except ValueError:
        print("Invalid input. Enter a digit.")
# Prompt the user to input values

# Calculate
