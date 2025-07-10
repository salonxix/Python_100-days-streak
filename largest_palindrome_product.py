def largestPalindrome(n: int) -> int:
    if n == 1:
        return 9

    upper = 10**n - 1
    lower = 10**(n - 1)

    for a in range(upper, lower - 1, -1):
        # Generate a palindrome from a
        pal = int(str(a) + str(a)[::-1])

        for b in range(upper, lower - 1, -1):
            if pal // b > upper:
                break
            if pal % b == 0:
                print(f"Palindrome {pal} = {b} x {pal//b}")
                return pal % 1337

    return -1  # Should never hit


# Example usage:
n = 2
result = largestPalindrome(n)
print(f"✅ Output for n = {n} → {result}")
