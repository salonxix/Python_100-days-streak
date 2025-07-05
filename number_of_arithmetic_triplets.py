def arithmeticTriplets(nums, diff):
    num_set = set(nums)
    count = 0

    for num in nums:
        if (num + diff in num_set) and (num + 2 * diff in num_set):
            count += 1

    return count

# 🔍 Test Cases
print(arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))  # Output: 2
print(arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))   # Output: 2
