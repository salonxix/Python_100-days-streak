from collections import defaultdict

def maximumEdgesToDelete(nums, edges):
    n = len(nums)
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    total = sum(nums)

    for k in range(n, 0, -1):
        if total % k != 0:
            continue
        target = total // k
        count = [0]

        def dfs(node, parent):
            curr_sum = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    curr_sum += dfs(nei, node)
            if curr_sum == target:
                count[0] += 1
                return 0  # We remove this edge
            return curr_sum

        dfs(0, -1)

        if count[0] == k:
            return k - 1  # We can make k parts by removing k-1 edges

    return 0

# 🔽 Run sample inputs
nums1 = [6, 2, 2, 2, 6]
edges1 = [[0, 1], [1, 2], [1, 3], [3, 4]]
print("Example 1 Output:", maximumEdgesToDelete(nums1, edges1))  # ➤ 2

nums2 = [2]
edges2 = []
print("Example 2 Output:", maximumEdgesToDelete(nums2, edges2))  # ➤ 0
