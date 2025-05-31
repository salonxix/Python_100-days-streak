def romanToInt(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s.upper()):  # Reverse for easier subtractive logic
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# 🚀 Take Roman numeral input from the user
roman_input = input("Enter a Roman numeral: ").upper()

# Validate Roman numeral
valid_roman_chars = set("IVXLCDM")
if all(c in valid_roman_chars for c in roman_input):
    result = romanToInt(roman_input)
    print(f"Integer value: {result}")
else:
    print("❌ Invalid Roman numeral! Use only I, V, X, L, C, D, M.")
