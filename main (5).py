# Day 6 of 100 Days of Python - Simple Interest Calculator

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest Calculator")
p = float(input("Enter principal amount: ₹"))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time in years: "))

interest = calculate_simple_interest(p, r, t)
print(f"Simple Interest = ₹{interest:.2f}")