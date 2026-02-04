# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # works fine unless num2 = 0

# Displaying results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

# Checking division by zero
if num2 != 0:
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")
