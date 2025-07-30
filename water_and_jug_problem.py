import math

def canMeasureWater(x, y, target):
    if target > x + y:
        return False
    if target == 0:
        return True
    return target % math.gcd(x, y) == 0

# Test cases
print("Example 1:", canMeasureWater(3, 5, 4))  # True
print("Example 2:", canMeasureWater(2, 6, 5))  # False
print("Example 3:", canMeasureWater(1, 2, 3))  # True
