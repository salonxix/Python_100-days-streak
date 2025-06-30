from collections import defaultdict

def minIncrements(n, edges, cost):
    # Step 1: Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: First DFS - get max cost path from root to any leaf
    def get_max_path_score(node, parent):
        if len(tree[node]) == 1 and parent != -1:  # it's a leaf
            return cost[node]
        max_child_path = 0
        for nei in tree[node]:
            if nei != parent:
                max_child_path = max(max_child_path, get_max_path_score(nei, node))
        return cost[node] + max_child_path

    max_score = get_max_path_score(0, -1)

    # Step 3: Second DFS - count increments needed
    increments = 0
    def dfs(node, parent, curr_sum):
        nonlocal increments
        children = [nei for nei in tree[node] if nei != parent]

        if not children:  # it's a leaf
            diff = max_score - (curr_sum + cost[node])
            if diff > 0:
                increments += 1
            return

        for nei in children:
            dfs(nei, node, curr_sum + cost[node])

    dfs(0, -1, 0)
    return increments

# 🔍 Example usage:
print(minIncrements(3, [[0,1],[0,2]], [2,1,3]))         # ➤ 1
print(minIncrements(3, [[0,1],[1,2]], [5,1,4]))         # ➤ 0
print(minIncrements(5, [[0,4],[0,1],[1,2],[1,3]], [3,4,1,1,7]))  # ➤ 1
