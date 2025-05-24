# Day 7 of 100 Days of Python - Even or Odd Checker

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(f"The number {n} is {check_even_odd(n)}.")