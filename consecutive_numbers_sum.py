def consecutiveNumbersSum(n: int) -> int:
    count = 0
    k = 1

    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            x = (n - k * (k - 1) // 2) // k
            print(f"n = {n}, k = {k}, x = {x} → Valid sequence: {[x + i for i in range(k)]}")
            count += 1
        k += 1

    return count

# Example usage
n = 15
result = consecutiveNumbersSum(n)
print(f"\n✅ Total ways to express {n} as sum of consecutive integers: {result}")
