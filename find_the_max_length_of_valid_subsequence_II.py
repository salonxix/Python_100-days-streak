def longestValidSubsequence(nums):
    # Case 1: all-same-parity subsequence (even‑sum pairs)
    count_even = sum(1 for x in nums if x % 2 == 0)
    count_odd  = len(nums) - count_even
    best_same = max(count_even, count_odd)
    
    # Case 2: alternating-parity subsequence (odd‑sum pairs)
    def alternating_length(start_parity):
        length = 0
        expected = start_parity
        for x in nums:
            if x % 2 == expected:
                length += 1
                expected ^= 1  # flip expectation
        return length
    
    best_alt = max(alternating_length(0), alternating_length(1))
    
    return max(best_same, best_alt)

# ———————— Test Cases ————————

print("Example 1:", longestValidSubsequence([1,2,3,4]))            # 4
print("Example 2:", longestValidSubsequence([1,2,1,1,2,1,2]))      # 6
print("Example 3:", longestValidSubsequence([1,3]))                # 2

# Additional tests
print("All evens:", longestValidSubsequence([2,4,6,8]))           # 4
print("Mixed:",    longestValidSubsequence([5,2,7,4,3,6,1,8,9]))  # e.g. 8
