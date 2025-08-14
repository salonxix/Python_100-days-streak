def isPowerOfThree(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Example usage
print(isPowerOfThree(27))  # True (27 = 3^3)
print(isPowerOfThree(0))   # False
print(isPowerOfThree(-1))  # False
