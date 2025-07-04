def countQuadruplets(nums):
    n = len(nums)
    count = 0
    
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1
    return count

# 🔍 Test Cases
print(countQuadruplets([1,2,3,6]))      # Output: 1
print(countQuadruplets([3,3,6,4,5]))    # Output: 0
print(countQuadruplets([1,1,1,3,5]))    # Output: 4
