from collections import Counter

def continuousSubarrays(nums):
    count = 0
    freq = Counter()
    start = 0

    for end in range(len(nums)):
        freq[nums[end]] += 1

        while max(freq) - min(freq) > 2:
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1

        count += end - start + 1

    return count

# 🔧 Example tests
print(continuousSubarrays([5, 4, 2, 4]))  # Output: 8
print(continuousSubarrays([1, 2, 3]))     # Output: 6
