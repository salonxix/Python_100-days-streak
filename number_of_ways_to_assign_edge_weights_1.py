from collections import defaultdict, deque

MOD = 10**9 + 7

def countOddCostAssignments(edges):
    # Step 1: Build the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: BFS to find max depth and a node at that depth
    n = len(edges) + 1
    depth = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    queue = deque()
    queue.append(1)
    depth[1] = 0

    max_depth = 0
    deepest_node = 1

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if depth[neighbor] == -1:
                depth[neighbor] = depth[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)
                if depth[neighbor] > max_depth:
                    max_depth = depth[neighbor]
                    deepest_node = neighbor

    # Step 3: Count number of edges from root to deepest_node
    d = 0
    node = deepest_node
    while parent[node] != -1:
        d += 1
        node = parent[node]

    # Step 4: Half of 2^d combinations have odd sum
    return pow(2, d - 1, MOD) if d > 0 else 1

# ✅ Sample Input
edges1 = [[1, 2]]
edges2 = [[1, 2], [1, 3], [3, 4], [3, 5]]

# ✅ Run and Print Output
print("Output for edges1:", countOddCostAssignments(edges1))  # Expected: 1
print("Output for edges2:", countOddCostAssignments(edges2))  # Expected: 2
