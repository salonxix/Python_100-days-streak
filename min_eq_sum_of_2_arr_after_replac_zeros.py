def min_equal_sum(nums1, nums2):
    sum1 = sum(x for x in nums1 if x != 0)
    sum2 = sum(x for x in nums2 if x != 0)
    
    zero1 = nums1.count(0)
    zero2 = nums2.count(0)
    
    # Minimum sum possible after replacements
    min_sum1 = sum1 + zero1  # all zeros replaced with 1
    min_sum2 = sum2 + zero2  # all zeros replaced with 1
    
    # The final sum must be at least max(min_sum1, min_sum2)
    final_sum = max(min_sum1, min_sum2)
    
    # Check if this final_sum satisfies the conditions:
    # (final_sum - sum1) >= zero1 and (final_sum - sum2) >= zero2
    if final_sum - sum1 >= zero1 and final_sum - sum2 >= zero2:
        return final_sum
    else:
        return -1


# Test with the provided examples
print(min_equal_sum([3,2,0,1,0], [6,5,0]))  # Output: 12
print(min_equal_sum([2,0,2,0], [1,4]))      # Output: -1
