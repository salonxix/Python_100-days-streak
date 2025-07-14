from collections import defaultdict
import heapq

def maxScore(scores, edges):
    n = len(scores)
    graph = defaultdict(list)

    # Build graph and store neighbors with max scores
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Precompute top 3 neighbors (by score) for each node
    top_neighbors = {}
    for node in range(n):
        neighbors = graph[node]
        neighbors.sort(key=lambda x: -scores[x])
        top_neighbors[node] = neighbors[:3]

    max_score = -1
    for u, v in edges:
        for a in top_neighbors[u]:
            if a == v:
                continue
            for b in top_neighbors[v]:
                if b == u or b == a:
                    continue
                total = scores[a] + scores[u] + scores[v] + scores[b]
                max_score = max(max_score, total)

    return max_score

# 🔽 Sample Inputs
print("Example 1 Output:", maxScore([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # ➤ 24
print("Example 2 Output:", maxScore([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]]))        # ➤ -1
