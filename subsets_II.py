def subsetsWithDup(nums):
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    nums.sort()  # Sort to handle duplicates
    result = []
    backtrack(0, [])
    return result

# 🚀 Test Cases
test_cases = [
    [1, 2, 2],
    [0],
    [1, 2, 2, 2],
    [4, 4, 4, 1, 4]
]

for i, nums in enumerate(test_cases):
    output = subsetsWithDup(nums)
    print(f"Test Case {i+1}: Input: {nums}")
    print(f"Output Subsets:")
    for subset in output:
        print(subset)
    print()
