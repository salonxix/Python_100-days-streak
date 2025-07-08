from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def is_good(number, k):
    str_num = str(number)
    seen = set()
    for perm in permutations(str_num):
        if perm in seen:
            continue
        seen.add(perm)
        if perm[0] == '0':  # leading zero check
            continue
        perm_num = int(''.join(perm))
        if is_palindrome(str(perm_num)) and perm_num % k == 0:
            return True
    return False

def countGoodNumbers(n, k):
    start = 10 ** (n - 1)
    end = 10 ** n
    count = 0
    for num in range(start, end):
        if is_good(num, k):
            count += 1
    return count

# 🔍 Test Cases
print(countGoodNumbers(3, 5))  # Output: 27
print(countGoodNumbers(1, 4))  # Output: 2
print(countGoodNumbers(5, 6))  # Output: 246
