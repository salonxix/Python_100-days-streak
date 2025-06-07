def climbStairs(n):
    if n <= 2:
        return n

    first, second = 1, 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second

# Example usage
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
