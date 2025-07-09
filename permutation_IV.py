from itertools import permutations

def is_alternating(perm):
    for i in range(len(perm) - 1):
        # If both even or both odd, invalid
        if (perm[i] % 2 == perm[i+1] % 2):
            return False
    return True

def getKthAlternatingPermutation(n, k):
    nums = list(range(1, n + 1))
    valid_perms = []

    for perm in permutations(nums):
        if is_alternating(perm):
            valid_perms.append(list(perm))

    valid_perms.sort()  # lexicographical sort

    if k <= len(valid_perms):
        return valid_perms[k - 1]
    return []

# 🔍 Test Cases
print(getKthAlternatingPermutation(4, 6))  # Output: [3, 4, 1, 2]
print(getKthAlternatingPermutation(3, 2))  # Output: [3, 2, 1]
print(getKthAlternatingPermutation(2, 3))  # Output: []
