from collections import defaultdict

def minimumScore(nums, edges):
    n = len(nums)
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    xor = [0] * n
    in_time = [0] * n
    out_time = [0] * n
    time = [0]

    # DFS to calculate subtree XORs and entry/exit times
    def dfs(node, parent):
        xor[node] = nums[node]
        time[0] += 1
        in_time[node] = time[0]
        for nei in tree[node]:
            if nei != parent:
                dfs(nei, node)
                xor[node] ^= xor[nei]
        time[0] += 1
        out_time[node] = time[0]

    dfs(0, -1)
    total = xor[0]
    res = float('inf')

    # Check if u is ancestor of v
    def is_ancestor(u, v):
        return in_time[u] < in_time[v] and out_time[u] > out_time[v]

    # Try all pairs of removed edges by iterating over nodes
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0 or j == 0:
                continue
            if is_ancestor(i, j):
                a = xor[j]
                b = xor[i] ^ xor[j]
                c = total ^ xor[i]
            elif is_ancestor(j, i):
                a = xor[i]
                b = xor[j] ^ xor[i]
                c = total ^ xor[j]
            else:
                a = xor[i]
                b = xor[j]
                c = total ^ xor[i] ^ xor[j]

            res = min(res, max(a, b, c) - min(a, b, c))

    return res

# Test Cases
print(minimumScore([1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]))  # Output: 9
print(minimumScore([5,5,2,4,4,2], [[0,1],[1,2],[5,2],[4,3],[1,3]]))  # Output: 0
