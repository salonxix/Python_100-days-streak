def addBinary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))

# Example runs
print(addBinary("11", "1"))     # Output: "100"
print(addBinary("1010", "1011")) # Output: "10101"
