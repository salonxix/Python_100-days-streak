def isPowerOfFour(n):
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1

# Taking input
n = int(input("Enter number: "))
print(isPowerOfFour(n))
