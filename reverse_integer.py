def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0

    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow
        if reversed_num > (INT_MAX - digit) // 10:
            return 0

        reversed_num = reversed_num * 10 + digit

    return sign * reversed_num

# Example usage:
if __name__ == "__main__":
    try:
        x = int(input("Enter a 32-bit signed integer: "))
        result = reverse(x)
        print("Reversed Integer:", result)
    except ValueError:
        print("Please enter a valid integer.")
