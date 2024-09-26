# Exercise 2: Ohm’s Law Calculator
    #Instructions:
        #1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
        #2.	Based on their choice, prompt the user to input the appropriate values.
        #3.	Use Ohm's Law to calculate the missing variable and display the result.
        #4.	Handle cases where division by zero might occur.

print("Welcome to Ohm's Law Calculator!\n")

# Ask the user what they want to calculate: Voltage, Current, or Resistance.
calculate = None
while calculate is None:
    try:
        calculate = int(input("What would you like to calculate?\n"
                              "1. Voltage\n"
                              "2. Current\n"
                              "3. Resistance\n"
                              "Enter here: "))
        if calculate not in [1, 2, 3]:
            print("Invalid input. Please enter numbers 1-3 only.\n")
            calculate = None
    except ValueError:
        print("Invalid input. Enter a number.\n")

# Prompt the user to input values
if calculate == 1:
    # Voltage
    while True:
        try:
            print('\nEnter Values for:')
            current = float(input("Current: "))
            resistance = float(input("Resistance: "))
            voltage = (current * resistance)
            print(f"Voltage = {voltage:.2f}")
        except ValueError:
              print("Invalid input. Enter number.")

elif calculate == 2:
      # Current
    while True:
        try:
            print('\nEnter Values for:')
            voltage = float(input("Voltage: "))
            resistance = float(input("Resistance: "))
            current = (voltage / resistance)
            print(f"Current = {current:.2f}")
            break
        except ZeroDivisionError:
             print("ERROR: Cannot divide by zero.")
        except ValueError:
             print("Invalid input. Enter number.")

elif calculate == 3:
    # Resistance
    while True:
        try:
            print('\nEnter Values for:')
            voltage = float(input("Voltage: "))
            current = float(input("Current: "))
            resistance = (voltage / current)
            print(f"Resistance = {resistance:.2f}")
            break
        except ZeroDivisionError:
             print("ERROR: Cannot divide by zero.")
        except ValueError:
             print("Invalid input. Enter number.")

else:
     print("Invalid input. Enter a valid option.")
