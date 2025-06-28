def titleToNumber(columnTitle: str) -> int:
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result


# ✅ Test Cases
if __name__ == "__main__":
    print(titleToNumber("A"))   # ➤ 1
    print(titleToNumber("AB"))  # ➤ 28
    print(titleToNumber("ZY"))  # ➤ 701
    print(titleToNumber("FXSHRXW"))  # ➤ Very large number (example stress test)
