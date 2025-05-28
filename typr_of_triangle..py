def triangleType(nums):
    a, b, c = nums[0], nums[1], nums[2]

    # Check for triangle validity
    if a + b <= c or a + c <= b or b + c <= a:
        return "none"

    # Check for triangle type
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

# Test cases
print(triangleType([3, 3, 3]))  # Output: equilateral
print(triangleType([3, 4, 5]))  # Output: scalene
print(triangleType([5, 5, 8]))  # Output: isosceles
print(triangleType([1, 2, 3]))  # Output: none
