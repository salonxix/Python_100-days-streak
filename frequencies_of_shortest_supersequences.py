from functools import lru_cache
from itertools import permutations
from collections import Counter

def get_freq(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    return freq

@lru_cache(None)
def scs(a, b):
    # Shortest Common Supersequence of two strings
    if not a: return b
    if not b: return a
    if a[0] == b[0]:
        return a[0] + scs(a[1:], b[1:])
    else:
        res1 = a[0] + scs(a[1:], b)
        res2 = b[0] + scs(a, b[1:])
        return res1 if len(res1) < len(res2) else res2

def combine_scs(words):
    from functools import reduce
    return reduce(scs, words)

def all_valid_scs(words):
    # BFS approach to generate all valid SCSs
    from collections import deque

    q = deque()
    q.append(("", 0))  # current string, word index
    seen = set()
    min_len = float('inf')
    results = set()

    while q:
        cur, idx = q.popleft()

        if idx == len(words):
            if len(cur) < min_len:
                min_len = len(cur)
                results = set([cur])
            elif len(cur) == min_len:
                results.add(cur)
            continue

        word = words[idx]
        def helper(i, j, path):
            if i == len(cur):
                return path + word[j:]
            if j == len(word):
                return cur[i:]

            if cur[i] == word[j]:
                return cur[i] + helper(i + 1, j + 1, path)
            else:
                option1 = cur[i] + helper(i + 1, j, path)
                option2 = word[j] + helper(i, j + 1, path)
                return option1 if len(option1) < len(option2) else option2

        merged = helper(0, 0, "")
        q.append((merged, idx + 1))

    return results

def shortest_common_supersequence_freqs(words):
    from itertools import permutations

    # Generate all permutations to try all possible orderings
    seen_freqs = set()
    result = []

    for perm in permutations(words):
        merged = combine_scs(perm)
        freq = tuple(get_freq(merged))
        if freq not in seen_freqs:
            seen_freqs.add(freq)
            result.append(list(freq))

    return result

# 🔍 Test Cases
print(shortest_common_supersequence_freqs(["ab", "ba"]))
# Output: [[1, 2, 0, ..., 0], [2, 1, 0, ..., 0]]

print(shortest_common_supersequence_freqs(["aa", "ac"]))
# Output: [[2, 0, 1, 0, ..., 0]]

print(shortest_common_supersequence_freqs(["aa", "bb", "cc"]))
# Output: [[2, 2, 2, 0, ..., 0]]
