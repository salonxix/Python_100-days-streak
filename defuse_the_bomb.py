def decrypt(code, k):
    n = len(code)
    result = [0] * n

    if k == 0:
        return result

    for i in range(n):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]
        else:  # k < 0
            for j in range(1, -k + 1):
                total += code[(i - j + n) % n]
        result[i] = total

    return result

# 🔧 Example tests
print(decrypt([5, 7, 1, 4], 3))   # Output: [12, 10, 16, 13]
print(decrypt([1, 2, 3, 4], 0))   # Output: [0, 0, 0, 0]
print(decrypt([2, 4, 9, 3], -2))  # Output: [12, 5, 6, 13]
