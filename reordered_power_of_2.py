def reorderedPowerOf2(n):
    def count_digits(num):
        return tuple(sorted(str(num)))
    
    # Precompute all powers of 2 up to 2^30
    power_of_2_counts = {count_digits(1 << i) for i in range(31)}
    
    return count_digits(n) in power_of_2_counts

# 🔍 Test Cases
print(reorderedPowerOf2(1))   # Output: True
print(reorderedPowerOf2(10))  # Output: False
print(reorderedPowerOf2(46))  # Output: True (because 64 is a power of 2)
print(reorderedPowerOf2(24))  # Output: True (42 → 2^5 = 32 is not possible, but 24 → 4^2 = 16 not valid, so False)
