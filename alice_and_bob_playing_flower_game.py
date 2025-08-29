def countWinningPairs(n, m):
    count = 0
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            # Alice wins if XOR is not zero
            if x ^ y != 0:
                count += 1
    return count


# Example runs
print(countWinningPairs(3, 2))  # Output: 3
print(countWinningPairs(1, 1))  # Output: 0
