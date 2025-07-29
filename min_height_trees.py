from collections import defaultdict

def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    # Step 1: Build the graph (adjacency list)
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Step 2: Initialize leaves (nodes with only one connection)
    leaves = [i for i in range(n) if len(graph[i]) == 1]

    # Step 3: Trim leaves layer by layer until <= 2 nodes remain
    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leaves = []

        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    # Step 4: Remaining 1 or 2 nodes are centroids (MHT roots)
    return leaves

# 🔹 Terminal Test Block
if __name__ == "__main__":
    # Example 1
    n1 = 4
    edges1 = [[1,0],[1,2],[1,3]]
    print("Example 1 Output:", findMinHeightTrees(n1, edges1))  # Expected: [1]

    # Example 2
    n2 = 6
    edges2 = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print("Example 2 Output:", findMinHeightTrees(n2, edges2))  # Expected: [3, 4]
