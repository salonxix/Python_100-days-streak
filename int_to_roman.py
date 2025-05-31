def intToRoman(num):
    val_sym_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
        (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
        (1, 'I')
    ]

    roman = ""
    for value, symbol in val_sym_map:
        while num >= value:
            roman += symbol
            num -= value

    return roman

# 🚀 Take input from the user
try:
    number = int(input("Enter an integer (1 to 3999): "))
    if 1 <= number <= 3999:
        result = intToRoman(number)
        print(f"Roman numeral: {result}")
    else:
        print("❌ Please enter a number between 1 and 3999.")
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
