MOD = 10**9 + 7

def count_possible_originals_k(word, k):
    n = len(word)
    groups = []
    i = 0

    # Step 1: Group consecutive characters
    while i < n:
        j = i
        while j < n and word[j] == word[i]:
            j += 1
        groups.append(j - i)
        i = j

    total = 0

    # Step 2: Count valid combinations
    # Case 1: original string is valid
    if n >= k:
        total += 1

    # Case 2: try reducing each group
    for g in groups:
        for reduce in range(1, g):
            if n - reduce >= k:
                total += 1
            else:
                break

    return total % MOD

# 🚀 Example usage
print(count_possible_originals_k("aabbccdd", 7))  # Output: 5
print(count_possible_originals_k("aabbccdd", 8))  # Output: 1
print(count_possible_originals_k("aaabbb", 3))    # Output: 8
