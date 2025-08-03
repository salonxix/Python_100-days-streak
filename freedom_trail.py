from collections import defaultdict
from functools import lru_cache

def findRotateSteps(ring, key):
    n = len(ring)
    char_indices = defaultdict(list)
    
    for i, ch in enumerate(ring):
        char_indices[ch].append(i)

    @lru_cache(None)
    def dfs(pos, idx):
        if idx == len(key):
            return 0
        res = float('inf')
        for i in char_indices[key[idx]]:
            dist = abs(i - pos)
            step = min(dist, n - dist)
            res = min(res, step + 1 + dfs(i, idx + 1))
        return res

    return dfs(0, 0)

# Example Usage:
ring1 = "godding"
key1 = "gd"
print(findRotateSteps(ring1, key1))  # Output: 4

ring2 = "godding"
key2 = "godding"
print(findRotateSteps(ring2, key2))  # Output: 13
