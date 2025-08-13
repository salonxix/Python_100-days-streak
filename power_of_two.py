def isPowerOfTwo(n: int) -> bool:
    # A number is a power of two if it's > 0 and has exactly one bit set in binary form
    return n > 0 and (n & (n - 1)) == 0


# Example usage
print(isPowerOfTwo(1))   # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(3))   # False
