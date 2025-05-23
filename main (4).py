# Day 6 of 100 Days of Python - Temperature Converter

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose (1/2): ")

if choice == '1':
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {c_to_f(c):.2f}°F")
elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F = {f_to_c(f):.2f}°C")
else:
    print("Invalid choice.")
