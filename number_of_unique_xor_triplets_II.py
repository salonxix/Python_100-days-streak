def countUniqueXORTriplets(nums):
    n = len(nums)
    xor_values = set()

    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                result = nums[i] ^ nums[j] ^ nums[k]
                xor_values.add(result)

    return len(xor_values)

# 🔍 Test Cases
print(countUniqueXORTriplets([1, 3]))          # Output: 2
print(countUniqueXORTriplets([6, 7, 8, 9]))    # Output: 4
print(countUniqueXORTriplets([0, 0, 0]))       # Output: 1 (only 0)
