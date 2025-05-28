from collections import Counter

def longestPalindrome(words):
    freq = Counter(words)
    length = 0
    used_center = False

    for word in list(freq.keys()):
        rev = word[::-1]

        if word == rev:
            # For symmetric words like "cc"
            pairs = freq[word] // 2
            length += pairs * 4
            freq[word] -= pairs * 2
        elif rev in freq:
            # For pairs like "lc" and "cl"
            pair_count = min(freq[word], freq[rev])
            length += pair_count * 4
            freq[word] -= pair_count
            freq[rev] -= pair_count

    # Check if there's any unused symmetric word for the center
    for word in freq:
        if word[0] == word[1] and freq[word] > 0:
            length += 2
            break

    return length

# Test cases
print(longestPalindrome(["lc","cl","gg"]))            # Output: 6
print(longestPalindrome(["ab","ty","yt","lc","cl","ab"]))  # Output: 8
print(longestPalindrome(["cc","ll","xx"]))            # Output: 2
