import math

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates the power (x^y)
def power(x, y):
    return x ** y

# This function calculates the square root (√x)
def square_root(x):
    return math.sqrt(x)

print("Select operation.")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Power (x^y)")
print("6. Square Root (√x)")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5/6): ")

    # Check if choice is valid
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            if choice != '6':  # Square root needs only one number
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            else:
                num1 = float(input("Enter the number for square root: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            if num1 < 0:
                print("Error! Square root of a negative number is not real.")
            else:
                print(f"√{num1} = {square_root(num1)}")

        # Ask if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid Input. Please enter a valid choice (1/2/3/4/5/6).")