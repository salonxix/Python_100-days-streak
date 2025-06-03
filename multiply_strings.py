def multiplyStrings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    # Initialize result array
    result = [0] * (len(num1) + len(num2))

    # Reverse both strings to multiply from least significant digit
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Multiply digit by digit
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            product = digit1 * digit2

            result[i + j] += product
            result[i + j + 1] += result[i + j] // 10  # carry
            result[i + j] = result[i + j] % 10

    # Remove leading zeros from the end (since result is reversed)
    while result[-1] == 0:
        result.pop()

    # Convert to string and reverse back
    return ''.join(map(str, result[::-1]))


# ------------ Example usage -------------
if __name__ == "__main__":
    test_cases = [
        ("2", "3"),           # Output: "6"
        ("123", "456"),       # Output: "56088"
        ("0", "456"),         # Output: "0"
        ("999", "999"),       # Output: "998001"
    ]

    for n1, n2 in test_cases:
        print(f"{n1} × {n2} = {multiplyStrings(n1, n2)}")
