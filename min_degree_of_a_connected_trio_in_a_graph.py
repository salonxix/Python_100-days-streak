from collections import defaultdict
from itertools import combinations

def minTrioDegree(n, edges):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
        degree[u] += 1
        degree[v] += 1

    res = float('inf')

    # Check all combinations of 3 nodes
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i][j]:
                for k in range(j + 1, n + 1):
                    if graph[i][k] and graph[j][k]:
                        # Trio found
                        curr_degree = degree[i] + degree[j] + degree[k] - 6
                        res = min(res, curr_degree)

    return res if res != float('inf') else -1

# 🔍 Example Usage:
n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
print(minTrioDegree(n, edges))  # Output: 3
