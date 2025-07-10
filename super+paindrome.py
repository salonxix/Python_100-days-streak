def is_palindrome(s):
    return s == s[::-1]

def superpalindromesInRange(left, right):
    left = int(left)
    right = int(right)
    count = 0

    # Generate palindromes and check their squares
    for k in range(1, 100000):
        s = str(k)
        
        # Odd length palindromes
        t = s + s[-2::-1]
        v = int(t) ** 2
        if v > right:
            break
        if v >= left and is_palindrome(str(v)):
            count += 1

        # Even length palindromes
        t = s + s[::-1]
        v = int(t) ** 2
        if v > right:
            continue
        if v >= left and is_palindrome(str(v)):
            count += 1

    return count

# Example Usage
print(superpalindromesInRange("4", "1000"))  # Output: 4
print(superpalindromesInRange("1", "2"))     # Output: 1
