from itertools import combinations
from math import prod

def can_partition(nums, target):
    n = len(nums)
    for i in range(1, n):  # Non-empty subset sizes
        for subset in combinations(nums, i):
            if prod(subset) == target:
                remaining = nums.copy()
                for num in subset:
                    remaining.remove(num)
                if remaining and prod(remaining) == target:
                    return True
    return False

# Example test cases
print(can_partition([3, 1, 6, 8, 4], 24))  # True
print(can_partition([2, 5, 3, 7], 15))     # False
