from collections import Counter

def longestSubsequenceRepeatedK(s: str, k: int) -> str:
    def isSubsequence(t):
        target = t * k
        j = 0
        for c in s:
            if c == target[j]:
                j += 1
                if j == len(target):
                    return True
        return False

    freq = Counter(s)
    chars = []
    for c in sorted(freq.keys(), reverse=True):
        if freq[c] >= k:
            chars.extend([c] * min(freq[c] // k, 2))

    result = ""

    def backtrack(path):
        nonlocal result
        if len(path) > 7:
            return
        if len(path) > len(result) or (len(path) == len(result) and path > result):
            if isSubsequence(path):
                result = path
        for c in chars:
            backtrack(path + c)

    backtrack("")
    return result


# Example inputs
s = "letsleetcode"
k = 2

# Print the result to the terminal
print(longestSubsequenceRepeatedK(s, k))
