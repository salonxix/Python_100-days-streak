import heapq

def minCostConnectPoints(points):
    n = len(points)
    visited = set()
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0

    while len(visited) < n:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost

        for v in range(n):
            if v not in visited:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (dist, v))

    return total_cost

# Example usage
points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points2 = [[3,12],[-2,5],[-4,1]]

print("Minimum cost to connect points 1:", minCostConnectPoints(points1))  # Output: 20
print("Minimum cost to connect points 2:", minCostConnectPoints(points2))  # Output: 18
