# Mini Calculator in Python

print("Welcome to the Mini Calculator!")

# Taking two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Asking the user to choose an operation
print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")

# Performing the selected operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation selected!"

print("Result:", result)