def distinctEchoSubstrings(text: str) -> int:
    n = len(text)
    seen = set()

    for i in range(n):
        for j in range(i+1, n+1):
            sub = text[i:j]
            if len(sub) % 2 == 0:  # only even length substrings
                mid = len(sub) // 2
                if sub[:mid] == sub[mid:]:
                    seen.add(sub)
    
    return len(seen)

# Example usage:
print(distinctEchoSubstrings("abcabcabc"))   # Output: 3
print(distinctEchoSubstrings("leetcodeleetcode"))  # Output: 2
