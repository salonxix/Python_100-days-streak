from collections import defaultdict, deque
from itertools import combinations

def countSubgraphsForEachDiameter(n, edges):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    res = [0] * (n - 1)

    # Step 2: Try every subset of nodes (except single-node subsets)
    for mask in range(1, 1 << n):
        nodes = [i for i in range(n) if (mask >> i) & 1]
        if len(nodes) < 2:
            continue

        # BFS to check if the subset forms a connected component
        def is_connected(nodes):
            visited = set()
            q = deque([nodes[0]])
            visited.add(nodes[0])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v in nodes and v not in visited:
                        visited.add(v)
                        q.append(v)
            return len(visited) == len(nodes)

        if not is_connected(nodes):
            continue

        # Step 3: Calculate max distance in subset
        def bfs(start):
            visited = set()
            q = deque([(start, 0)])
            visited.add(start)
            farthest = (start, 0)
            while q:
                u, d = q.popleft()
                if d > farthest[1]:
                    farthest = (u, d)
                for v in graph[u]:
                    if v in nodes and v not in visited:
                        visited.add(v)
                        q.append((v, d + 1))
            return farthest

        node1, _ = bfs(nodes[0])
        _, dist = bfs(node1)
        res[dist - 1] += 1

    return res

# 🔍 Example Usage:
n = 4
edges = [[1,2],[2,3],[2,4]]
print(countSubgraphsForEachDiameter(n, edges))  # Output: [3, 4, 0]
