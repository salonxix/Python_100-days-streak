def convertToTitle(columnNumber: int) -> str:
    result = []

    while columnNumber > 0:
        columnNumber -= 1  # Adjust to 0-based indexing
        remainder = columnNumber % 26
        result.append(chr(65 + remainder))  # Convert to letter
        columnNumber //= 26

    return ''.join(reversed(result))


# ✅ Test Cases
if __name__ == "__main__":
    print(convertToTitle(1))     # ➤ "A"
    print(convertToTitle(28))    # ➤ "AB"
    print(convertToTitle(701))   # ➤ "ZY"
    print(convertToTitle(52))    # ➤ "AZ"
