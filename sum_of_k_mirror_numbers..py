def is_palindrome(s):
    return s == s[::-1]

def to_base_k(n, k):
    res = []
    while n > 0:
        res.append(str(n % k))
        n //= k
    return ''.join(reversed(res))

def generate_palindromes():
    # Generate palindromes in base 10
    num = 1
    while True:
        # Odd length palindromes
        s = str(num)
        yield int(s + s[-2::-1])  # like 121, 131
        # Even length palindromes
        yield int(s + s[::-1])    # like 11, 1221
        num += 1

def k_mirror(k, n):
    gen = generate_palindromes()
    count = 0
    total = 0
    seen = set()

    while count < n:
        num = next(gen)
        base_k = to_base_k(num, k)
        if is_palindrome(base_k):
            total += num
            count += 1

    return total

# Example Usage
k = 2
n = 5
print("Output:", k_mirror(k, n))
