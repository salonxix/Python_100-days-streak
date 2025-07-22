def divisorSubstrings(num: int, k: int) -> int:
    num_str = str(num)
    count = 0

    for i in range(len(num_str) - k + 1):
        sub = int(num_str[i:i + k])
        if sub != 0 and num % sub == 0:
            count += 1

    return count

# 🔧 Example tests
print(divisorSubstrings(240, 2))      # Output: 2
print(divisorSubstrings(430043, 2))   # Output: 2
