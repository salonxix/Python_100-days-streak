# Day 97 - Phone Number Validation

import re

def valid_phone_numbers(filename):
    # Define regex for valid phone numbers
    pattern = re.compile(r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")
    
    with open(filename, 'r') as file:
        for line in file:
            number = line.strip()
            if pattern.match(number):
                print(number)


# Example usage
if __name__ == "__main__":
    valid_phone_numbers("file.txt")
