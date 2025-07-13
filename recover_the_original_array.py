from collections import Counter

def recoverArray(nums):
    nums.sort()
    n = len(nums)

    for i in range(1, n):
        diff = nums[i] - nums[0]
        if diff == 0 or diff % 2 != 0:
            continue

        k = diff // 2
        count = Counter(nums)
        result = []

        for num in nums:
            if count[num] == 0:
                continue
            if count[num + 2 * k] == 0:
                break
            result.append(num + k)
            count[num] -= 1
            count[num + 2 * k] -= 1

        if len(result) == n // 2:
            return result

    return []

# 🔽 Sample Inputs to test
test_cases = [
    [2,10,6,4,8,12],
    [1,1,3,3],
    [5,435]
]

for idx, nums in enumerate(test_cases):
    print(f"Example {idx + 1}:")
    print("Input nums:", nums)
    result = recoverArray(nums)
    print("Recovered arr:", result)
    print("-" * 30)
