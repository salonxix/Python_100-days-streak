def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""

    char_set = set(s)
    for i in range(len(s)):
        if s[i].swapcase() not in char_set:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right

    return s

# 🔧 Example tests
print(longestNiceSubstring("YazaAay"))  # Output: "aAa"
print(longestNiceSubstring("Bb"))       # Output: "Bb"
print(longestNiceSubstring("c"))        # Output: ""
