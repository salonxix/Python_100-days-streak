def isThree(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    
    root = int(n ** 0.5)
    return root * root == n and is_prime(root)

# Test cases
print(isThree(2))  # False
print(isThree(4))  # True
print(isThree(9))  # True (divisors: 1, 3, 9)
