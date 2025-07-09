def minimize_max_identical_substring(s: str, numOps: int) -> int:
    def canAchieve(maxLen: int) -> bool:
        # Returns True if we can make all blocks of identical chars <= maxLen with ≤ numOps
        ops_needed = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            count = j - i
            if count > maxLen:
                # How many flips needed to split this long block
                ops_needed += (count - 1) // maxLen
            i = j
        return ops_needed <= numOps

    left, right = 1, len(s)
    answer = len(s)

    while left <= right:
        mid = (left + right) // 2
        if canAchieve(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# 🔍 Test Cases
print(minimize_max_identical_substring("000001", 1))  # Output: 2
print(minimize_max_identical_substring("0000", 2))    # Output: 1
print(minimize_max_identical_substring("0101", 0))    # Output: 1
