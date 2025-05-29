from typing import List

def maxTargetNodes(edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
    def build_graph(edges):
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g

    def get_parity_counts(g):
        n = len(g)
        color = [-1] * n
        counts = [0, 0]
        def dfs(u, c):
            color[u] = c
            counts[c] += 1
            for v in g[u]:
                if color[v] == -1:
                    dfs(v, c ^ 1)
        dfs(0, 0)
        return color, counts

    g1 = build_graph(edges1)
    g2 = build_graph(edges2)
    color1, counts1 = get_parity_counts(g1)
    color2, counts2 = get_parity_counts(g2)

    answer = []
    for u in range(len(g1)):
        # Try connecting u to either parity group in tree2 for the best result
        max_targets = max(
            counts1[color1[u]] + counts2[0],
            counts1[color1[u]] + counts2[1]
        )
        answer.append(max_targets)
    return answer

# Example usage (from your screenshot)
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
print(maxTargetNodes(edges1, edges2))  # Output: [8, 7, 7, 8, 8]
