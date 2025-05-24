# Day 7 of 100 Days of Python - Leap Year Checker

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if is_leap(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")