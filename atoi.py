from collections import Counter

# Day 13: String to Integer (myAtoi)
def myAtoi(s: str) -> int:
    s = s.lstrip()  # Remove leading whitespaces
    if not s:
        return 0

    sign = 1
    index = 0
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    result *= sign

    # Clamp to 32-bit signed integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    return max(INT_MIN, min(INT_MAX, result))


# Day 11: Longest Palindrome Using Two-Letter Words
def longestPalindrome(words) -> int:
    count = Counter(words)
    length = 0
    center_used = False

    for word in list(count.keys()):
        rev = word[::-1]
        if word == rev:
            # Symmetric word, e.g., 'gg'
            pairs = count[word] // 2
            length += pairs * 4
            count[word] -= pairs * 2
            if count[word] > 0 and not center_used:
                length += 2
                center_used = True
        else:
            # Non-symmetric pairs, e.g., 'ab' + 'ba'
            pairs = min(count[word], count[rev])
            length += pairs * 4
            count[word] -= pairs
            count[rev] -= pairs

    return length


# User Input Section
if __name__ == "__main__":
    print("\n--- Day 13: String to Integer (myAtoi) ---")
    s = input("Enter a string to convert to integer: ").strip()
    result_atoi = myAtoi(s)
    print("Converted Integer:", result_atoi)

    print("\n--- Day 11: Longest Palindrome Using Two-Letter Words ---")
    words_input = input("Enter words (comma-separated, e.g., ab,ty,yt,lc,cl,ab): ").split(',')
    words_list = [word.strip() for word in words_input if word.strip()]
    result_palindrome = longestPalindrome(words_list)
    print("Longest Palindrome Length:", result_palindrome)
