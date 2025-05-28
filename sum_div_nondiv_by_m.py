def differenceOfSums(n, m):
    num1 = 0  # Sum of numbers not divisible by m
    num2 = 0  # Sum of numbers divisible by m

    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i

    return num1 - num2

# Test cases
print(differenceOfSums(10, 3))  # Output: 19
print(differenceOfSums(5, 6))   # Output: 15
print(differenceOfSums(5, 1))   # Output: -15
