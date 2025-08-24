def sumScores(s):
    n = len(s)
    Z = [0] * n
    l, r = 0, 0

    # Build Z-array
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1

    # Sum of Z-values + full string
    return sum(Z) + n


# Example runs
print(sumScores("babab"))     # Output: 9
print(sumScores("azbazbzaz")) # Output: 14
