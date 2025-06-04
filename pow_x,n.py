def myPow(x: float, n: int) -> float:
    def fastPow(base, exponent):
        if exponent == 0:
            return 1
        half = fastPow(base, exponent // 2)
        if exponent % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        x = 1 / x
        n = -n
    return fastPow(x, n)

# Example usage
print(myPow(2.00000, 10))   # Output: 1024.0
print(myPow(2.10000, 3))    # Output: 9.261
print(myPow(2.00000, -2))   # Output: 0.25
